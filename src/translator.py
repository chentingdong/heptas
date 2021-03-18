import os
from typing import ByteString
import tensorflow as tf
from googletrans import Translator as GoogleTrans
import boto3
from ..configs.config import cfg
from ..configs.google_languages import GOOGLE_LANGUAGES
from ..configs.google_languages import GOOGLE_GLOSSARY
from ..configs.aws_languages import AWS_LANGUAGES
from .tokenizor import Tokenizer
from .logger import translation_logger as logger
import six
from google.cloud import translate_v2 as GCTranslate_v2
from google.cloud import translate as GCTranslate



class Translator(object):
    def __init__(
        self,
        model_dir=None,
        engine=cfg["translate"]["engine"],
        sourceLanguageCode=cfg["translate"]["sourceLanguageCode"],
        targetLanguageCode=cfg["translate"]["targetLanguageCode"],
        glossary=None,
    ):
        logger.info("Translation engine {} loaded.".format(engine))
        if engine == "google":
            self.translator = GoogleTranslator()
        elif engine == "aws" or engine == "amazon":
            self.translator = AwsTranslator(
                sourceLanguageCode=sourceLanguageCode,
                targetLanguageCode=targetLanguageCode
            )
        elif engine == "gc" or engine == 'Google Cloud':
            if glossary:
                self.translator = GoogleCloudTranslator_with_glossary(
                    sourceLanguageCode=sourceLanguageCode,
                    targetLanguageCode=targetLanguageCode,
                    glossary=glossary,
                )
            else:
                self.translator = GoogleCloudTranslator(
                    sourceLanguageCode=sourceLanguageCode,
                    targetLanguageCode=targetLanguageCode,
                    )
        elif engine == "bt" or engine == "biotranscribe":
            self.translator = BTTranslator(model_dir)

    def translate(self, text):
        return self.translator.translate(text)

class GoogleCloudTranslator_with_glossary:
    def __init__(
        self,
        sourceLanguageCode=cfg["translate"]["sourceLanguageCode"],
        targetLanguageCode=cfg["translate"]["targetLanguageCode"],
        glossary = "",
    ):
        self.translator = GCTranslate.TranslationServiceClient()
        self.sourceLanguageCode = sourceLanguageCode
        self.targetLanguageCode = targetLanguageCode
        if glossary:
            g = self.translator.glossary_path(
                GOOGLE_GLOSSARY["project_id"],
                GOOGLE_GLOSSARY["location"],
                glossary,
                )
            self.g_config = GCTranslate.TranslateTextGlossaryConfig(glossary=g)
        else:
            g = self.translator.glossary_path(
                GOOGLE_GLOSSARY["project_id"],
                GOOGLE_GLOSSARY["location"],
                GOOGLE_GLOSSARY["glossary_id"],
                )
            self.g_config = GCTranslate.TranslateTextGlossaryConfig(glossary=g)


    def translate(self, text) -> str:
        if len(text) == 0:
            return ""
        try:
            response = self.translator.translate_text(
                request={
                    "contents": [text],
                    "target_language_code": self.targetLanguageCode,
                    "source_language_code": self.sourceLanguageCode,
                    "parent": GOOGLE_GLOSSARY['parent'],
                    "glossary_config": self.g_config,
                    }
                )
            result = response.glossary_translations[0].translated_text

        except Exception as error:
            logger.error("GOOGLE Cloud translation failed, {}".format(error))
            result = " [N.A] "
        return result


class GoogleCloudTranslator:
    def __init__(
        self,
        sourceLanguageCode=cfg["translate"]["sourceLanguageCode"],
        targetLanguageCode=cfg["translate"]["targetLanguageCode"],
    ):
        self.translator = GCTranslate_v2.Client()
        self.sourceLanguageCode = sourceLanguageCode
        self.targetLanguageCode = targetLanguageCode

    def translate(self, text) -> str:
        if len(text) == 0:
            return ""
        try:
            #logger.debug("Target Language = {}".format(self.targetLanguageCode))
            translation = self.translator.translate(
                text,
                target_language=self.targetLanguageCode
            )
            result = translation["translatedText"]
        except Exception as error:
            logger.error("GOOGLE Cloud translation failed, {}".format(error))
            result = " [N.A] "
        return result



class AwsTranslator:
    def __init__(
        self,
        sourceLanguageCode=cfg["translate"]["sourceLanguageCode"],
        targetLanguageCode=cfg["translate"]["targetLanguageCode"],
    ):
        self.translator = boto3.client(
            service_name="translate",
            region_name=cfg["aws"]["region"],
            use_ssl=True,
        )
        self.sourceLanguageCode = AWS_LANGUAGES[sourceLanguageCode]
        self.targetLanguageCode = AWS_LANGUAGES[targetLanguageCode]

    def translate(self, text):
        if len(text) == 0:
            return ""
        try:
            translation = self.translator.translate_text(
                Text=text,
                SourceLanguageCode=self.sourceLanguageCode,
                TargetLanguageCode=self.targetLanguageCode
            )
            result = translation.get("TranslatedText")
        except Exception as error:
            logger.error("AWS translation failed, {}".format(error))
            result = " [N/A] "
        return result


class GoogleTranslator:
    def __init__(
        self,
        sourceLanguageCode=cfg["translate"]["sourceLanguageCode"],
        targetLanguageCode=cfg["translate"]["targetLanguageCode"],
    ):
        self.translator = GoogleTrans()
        self.sourceLanguageCode = GOOGLE_LANGUAGES[sourceLanguageCode]
        self.targetLanguageCode = GOOGLE_LANGUAGES[targetLanguageCode]

    def translate(self, text) -> str:
        if len(text) == 0:
            return ""
        translation = self.translator.translate(
            text,
            src=self.sourceLanguageCode,
            dest=self.targetLanguageCode,
        )
        result = translation.text
        return result


class BTTranslator:
    def __init__(self, model_dir=None):
        if model_dir is None:
            return
        self.model_dir = model_dir
        self.load_model(model_dir)

    def get_session(self):
        config = tf.compat.v1.ConfigProto()
        config.gpu_options.allow_growth = True
        return tf.compat.v1.Session(config=config)

    def load_model(self, model_dir):
        tf.compat.v1.keras.backend.set_session(self.get_session())
        imported = tf.saved_model.load(model_dir)
        self.translate_fn = imported.signatures["serving_default"]
        self.model_path = os.path.join(
            model_dir, "assets.extra", "source_tokenizer_config.yml"
        )

    def translate(self, text) -> str:
        tokenizer = Tokenizer([self.model_path])
        inputs = tokenizer.process([text])
        outputs = self.translate_fn(**inputs)
        result = tokenizer.postprocess(outputs)
        return result
