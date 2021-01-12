from ..src.docx_processor import DocxProcessor


def test_docx_processor():
    project = {
        "name": "demo 01",
        "engine": "aws",
        "docs": [
            {
                "sourceLanguageCode": "zh-cn",
                "targetLanguageCode": "en",
                "file": "NC PD Report Sample.docx",
            },
            {
                "sourceLanguageCode": "en",
                "targetLanguageCode": "zh-cn",
                "file": "NC Tox Report Sample.docx",
            },
            {
                "sourceLanguageCode": "zh-cn",
                "targetLanguageCode": "en",
                "file": "2013106976997.docx",
            },
            {
                "sourceLanguageCode": "zh-cn",
                "targetLanguageCode": "en",
                "file": "2014101200325.docx",
            },
        ],
    }

    for doc in project["docs"]:
        processor = DocxProcessor(
            doc["file"],
            engine=project["engine"],
            sourceLanguageCode=doc["sourceLanguageCode"],
            targetLanguageCode=doc["targetLanguageCode"],
        )
        result = processor.translate_doc()
        assert result == True
