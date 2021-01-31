from ..src.project_reporting import DocxReporting
import pytest

@pytest.mark.skip(reason="demo 1")
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

def test_docx_reporting_d2():
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
    reporter = DocxReporting(project['name'], project['docs'])
    result = reporter.report_csv()
    assert result == True

