from arrival.src.docx_processor import DocxProcessor


def test_docx_processor():
    translator_engine = "aws"
    docs = [
        "中医药现代化研究.1.docx",
    ]

    for doc in docs:
        processor = DocxProcessor(doc, engine=translator_engine)
        result = processor.translate_doc()
        assert result == True
