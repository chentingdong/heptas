from google.cloud import translate_v2

# define client
translate_client = translate_v2.Client()

#create function to translate text to English
def translated_test(text, target='en'):
    result = translate_client.translate(text, target_language=target)

    print('Translation', result['translatedText'])
    print('Source language: ', result['detectedSourceLanguage'])

text_test = 'Hola amigo'
translated_test(text_test)
