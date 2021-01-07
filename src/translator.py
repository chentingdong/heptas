import os
from typing import ByteString
import tensorflow as tf
from googletrans import Translator as GoogleTrans
import boto3
from ..configs.config import cfg
from ..configs.google_languages import GOOGLE_LANGUAGES
from ..configs.aws_languages import AWS_LANGUAGES
from .tokenizor import Tokenizer
from .logger import translation_logger as logger


class Translator(object):
    def __init__(self, model_dir=None, engine=None):
        engine = engine if engine is not None else cfg["translate"]["engine"]
        logger.info("Translation engine {} loaded.".format(engine))
        if engine == "google":
            self.translator = GoogleTranslator()
        elif engine == "aws" or engine == "amazon":
            self.translator = AwsTranslator()
        elif engine == "bt" or engine == "biotranscribe":
            self.translator = BTTranslator(model_dir)

    def translate(self, text):
        return self.translator.translate(text)


class AwsTranslator:
    def __init__(self):
        self.translator = boto3.client(
            service_name="translate", region_name=cfg["aws"]["region"], use_ssl=True
        )
        self.src_language = cfg["translate"]["sourceLanguageCode"]
        self.dest_language = cfg["translate"]["targetLanguageCode"]

    def translate(self, text):
        if len(text) == 0:
            return ""
        try:
            translation = self.translator.translate_text(
                Text=text,
                SourceLanguageCode=AWS_LANGUAGES[self.src_language],
                TargetLanguageCode=AWS_LANGUAGES[self.dest_language],
            )
            result = translation.get("TranslatedText")
        except Exception as error:
            logger.error("AWS translation failed, {}".format(error))
            result = " [N/A] "
        return result


class GoogleTranslator:
    def __init__(self):
        self.translator = GoogleTrans()
        self.src_language = GOOGLE_LANGUAGES[cfg["translate"]["sourceLanguageCode"]]
        self.dest_language = GOOGLE_LANGUAGES[cfg["translate"]["targetLanguageCode"]]

    def translate(self, text) -> str:
        if len(text) == 0:
            return ""
        translation = self.translator.translate(
            text,
            src=self.src_language,
            dest=self.dest_language,
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
