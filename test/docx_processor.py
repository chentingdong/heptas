from ..src.docx_processor import DocxProcessor


def test_docx_processor():
    project = {
        'name': 'demo 01',
        'engine': 'aws',
        'docs': [
            "2013106976997.docx",
            "2014101200325.docx"
        ]
    }

    for doc in project['docs']:
        processor = DocxProcessor(doc, engine=project['engine'])
        result = processor.translate_doc()
        assert result == True
