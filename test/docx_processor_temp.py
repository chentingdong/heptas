from ..src.docx_processor import DocxProcessor


def test_docx_processor():
    project = {
        "name": "demo 01",
        "engine": "aws",
        "docs": [
            {
                "sourceLanguageCode": "zh-cn",
                "targetLanguageCode": "en",
                "file": '2.6.7 毒理学试验列表-LY03009-20210122.docx',
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
