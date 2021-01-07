from ..src.project_reporting import DocxReporting


def test_docx_reporting():
    project = '20200106'
    docs = [
        "冠状病毒诊断技术国际专利布局分析.docx",
        "国家基本医疗保险.docx"
    ]
    
    reporter = DocxReporting(project, docs)
    result = reporter.report_csv()
    assert result == True
