from arrival.src.docx_processor import DocxProcessor


docs = [
    "../data/input/中医药现代化研究.1.docx",
    "../data/input/中医药预防感冒常用方法.docx",
]


def test_docx_processor():
    for doc in docs:
        processor = DocxProcessor(doc)
        result = processor.translate()
        assert result == True
