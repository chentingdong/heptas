from ..src.docx_process import DocxProcessor


def test_docx_translation():
    processor = DocxProcessor("../data/input/中医药现代化研究.docx")
    result = processor.translate("../data/output/中医药现代化研究.dest.docx")
    assert result