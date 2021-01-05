import os
from typing import ByteString
import tensorflow as tf
from ..configs.config import cfg
from ..configs.languages import LANGUAGES
from .tokenizor import Tokenizer
from googletrans import Translator as GoogleTrans
import boto3


class Translator(object):
    def __init__(self, model_dir=None, engine=None):
        engine = engine if engine is not None else cfg["translate"]["engine"]
        if engine == "google":
            self.translator = GoogleTranslator()
        elif engine == "aws":
            self.translator = AwsTranslator()
        elif engine == "biotranscribe":
            self.translator = BTTranslator(model_dir)

    def translate(self, text):
        return self.translator.translate(text)


class AwsTranslator:
    def __init__(self):
        self.translator = boto3.client(
            service_name="translate", region_name="region", use_ssl=True
        )

    def translate(self, text):
        return self.translator.translate_text(
            Text=text,
            SourceLanguageCode=cfg["translate"]["sourceLanguageCode"],
            TargetLanguageCode=cfg["translate"]["targetLanguageCode"],
        )


class GoogleTranslator:
    def __init__(self):
        self.translator = GoogleTrans()
        self.src_language = LANGUAGES[cfg["translate"]["sourceLanguageCode"]]
        self.dest_language = LANGUAGES[cfg["translate"]["targetLanguageCode"]]

    def translate(self, text) -> str:
        translation = self.translator.translate(
            text,
            src=self.src_language,
            dest=self.dest_language,
        )
        return translation.text


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
