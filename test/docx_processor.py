from ..src.docx_processor import DocxProcessor
import pytest

@pytest.mark.skip(reason="Demo 01")
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


def test_docx_processor_demo2():
    project = {
        "name": "demo 02",
        "engine": "gc",
        "docs": [
            {
                "sourceLanguageCode": "zh-cn",
                "targetLanguageCode": "en",
                "file": 'CL test 1_整体安全性评估.docx',
            },
            {
                "sourceLanguageCode": "zh-cn",
                "targetLanguageCode": "en",
                "file": 'CL test 2_研究方案.docx',
            },
            {
                "sourceLanguageCode": "zh-cn",
                "targetLanguageCode": "en",
                "file": 'CMC test 3_SHARK 报告 细胞株构建.docx',
            },
            {
                "sourceLanguageCode": "zh-cn",
                "targetLanguageCode": "en",
                "file": 'CMC test 4_SHARK 自由巯基报告.docx',
            },
            {
                "sourceLanguageCode": "zh-cn",
                "targetLanguageCode": "en",
                "file": 'CMC test 5-SHARK细胞培养工艺描述 30116-R2.docx',
            },
            {
                "sourceLanguageCode": "zh-cn",
                "targetLanguageCode": "en",
                "file": 'CMC test 6-SHARK项目纯化工艺描述R2.docx',
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


@pytest.mark.skip(reason="test GC")
def test_docx_processor_gc():
    project = {
        "name": "demo 01",
        "engine": "gc",
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

