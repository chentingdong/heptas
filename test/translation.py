from ..src.docx_processor import DocxProcessor


def test_docx_processor():
    processor = DocxProcessor("../data/input/中医药现代化研究.1.docx")
    result = processor.translate("../data/output/中医药现代化研究.1.dest.docx")
    assert result