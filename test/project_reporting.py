from ..src.project_reporting import DocxReporting


def test_docx_reporting():
    project = {
        'name': 'demo 01',
        'engine': 'aws',
        'docs': [
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
        ]
    }
    
    reporter = DocxReporting(project['name'], project['docs'])
    result = reporter.report_csv()
    assert result == True
