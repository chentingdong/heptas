from google.cloud import translate_v3 as translate


def get_glossary(project_id="YOUR_PROJECT_ID", glossary_id="YOUR_GLOSSARY_ID"):
    """Get a particular glossary based on the glossary ID."""

    client = translate.TranslationServiceClient()

    name = client.glossary_path(project_id, "us-central1", glossary_id)

    response = client.get_glossary(name=name)
    print(u"Glossary name: {}".format(response.name))
    print(u"Entry count: {}".format(response.entry_count))
    print(u"Input URI: {}".format(response.input_config.gcs_source.input_uri))


    #from google.cloud import translate


def list_glossaries(project_id="YOUR_PROJECT_ID"):
    """List Glossaries."""

    client = translate.TranslationServiceClient()

    location = "us-central1"

    parent = f"projects/{project_id}/locations/{location}"

    # Iterate over all results
    for glossary in client.list_glossaries(parent=parent):
        print("Name: {}".format(glossary.name))
        print("Entry count: {}".format(glossary.entry_count))
        print("Input uri: {}".format(glossary.input_config.gcs_source.input_uri))

        # Note: You can create a glossary using one of two modes:
        # language_code_set or language_pair. When listing the information for
        # a glossary, you can only get information for the mode you used
        # when creating the glossary.
        for language_code in glossary.language_codes_set.language_codes:
            print("Language code: {}".format(language_code))




def delete_glossary(
    project_id="YOUR_PROJECT_ID",
    glossary_id="YOUR_GLOSSARY_ID",
    timeout=180,
):
    """Delete a specific glossary based on the glossary ID."""
    client = translate.TranslationServiceClient()

    name = client.glossary_path(project_id, "us-central1", glossary_id)

    operation = client.delete_glossary(name=name)
    result = operation.result(timeout)
    print("Deleted: {}".format(result.name))


list_glossaries(415574831314)
get_glossary(415574831314, 'bt-zh-en-LetPub-glossary')
