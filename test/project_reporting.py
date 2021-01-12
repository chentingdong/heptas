from ..src.project_reporting import DocxReporting


def test_docx_reporting():
    project = {
        'name': 'demo 01',
        'engine': 'aws',
        'docs': [
            "2013106976997.docx",
            "2014101200325.docx"
        ]
    }
    
    reporter = DocxReporting(project, project.docs)
    result = reporter.report_csv()
    assert result == True
