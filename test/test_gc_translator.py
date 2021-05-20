from google.cloud import translate_v2
from ..src.translator import Translator
def test_translate_with_glossary(text='持续释放', source='zh-cn', target='en'):
    translator = Translator(
        engine='gc',
        sourceLanguageCode=source,
        targetLanguageCode=target,
        glossary='bt-zh-en-LetPub-glossary'
        )
    result = translator.translate(text)
    print('result=', result)
    print("\n")

    #for translation in result.translations:
    #    print("Translated text: {}".format(translation.translated_text))
    #for translation in result.glossary_translations:
    #    print("\t {}".format(translation.translated_text))

    assert True





