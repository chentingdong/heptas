from ..src.docx_processor import DocxProcessor


def test_docx_processor():
    translator_engine = "aws"
    docs = [
        "冠状病毒诊断技术国际专利布局分析.docx",
        "国家基本医疗保险.docx"
    ]

    for doc in docs:
        processor = DocxProcessor(doc, engine=translator_engine)
        result = processor.translate_doc()
        assert result == True
