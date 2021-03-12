from google.cloud import translate_v2
from ..src.translator import Translator


#create function to translate text to English
def test_translated(text='Hola amigo', target='en'):

    translate_client = translate_v2.Client()
    result = translate_client.translate(text, target_language=target)

    print('Translation', result['translatedText'])
    print('Source language: ', result['detectedSourceLanguage'])
    assert True

def test_translate_with_glossary(text='今晚的月亮真圆。'):
    translator = Translator(
        engine='gc',
        sourceLanguageCode='zh-cn',
        targetLanguageCode='en',
        glossary='bt-zh-en-LetPub-glossary'
        )
    result = translator.translate(text)
    print(result)
    print("\n")

    #for translation in result.translations:
    #    print("Translated text: {}".format(translation.translated_text))
    #for translation in result.glossary_translations:
    #    print("\t {}".format(translation.translated_text))

    assert True

#text_test = 'Hola amigo'
#translated_test(text_test)

#text_test = '今晚的月亮真圆。'
#translate_with_glossary(text_test)
