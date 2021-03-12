
from google.cloud import translate


def translate_text_with_glossary(
    text="羟基喜树碱 N-羟乙酰神经氨酸 N蛋白 N-聚糖酶",
    project_id="415574831314",
    glossary_id="bt-zh-en-LetPub-glossary",
):
    """Translates a given text using a glossary."""

    client = translate.TranslationServiceClient()
    location = "us-central1"
    parent = f"projects/{project_id}/locations/{location}"

    glossary = client.glossary_path(
        project_id, "us-central1", glossary_id  # The location of the glossary
    )

    glossary_config = translate.TranslateTextGlossaryConfig(glossary=glossary)

    # Supported language codes: https://cloud.google.com/translate/docs/languages
    response = client.translate_text(
        request={
            "contents": [text],
            "target_language_code": "en",
            "source_language_code": "zh",
            "parent": parent,
            "glossary_config": glossary_config,
        }
    )
    print(response)

    print("Translated text: \n")
    for translation in response.glossary_translations:
        print("\t {}".format(translation.translated_text))

translate_text_with_glossary()
