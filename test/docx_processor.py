from ..src.docx_processor import DocxProcessor
from ..configs.config import generate_project_config
import pytest

def test_docx_processor(project_config_pro5):
    project = project_config_pro5
    for doc in project["docs"]:
        processor = DocxProcessor(
            doc["file"],
            engine=project["engine"],
            sourceLanguageCode=doc["sourceLanguageCode"],
            targetLanguageCode=doc["targetLanguageCode"],
        )
        result = processor.translate_doc()
        assert result == True


def test_fixture():
    docs=["fil1.docx", "file2.docx"]
    project = generate_project_config("test_fixture", "gc", docs, "zh-cn", "en")
    assert project["name"] == "test_fixture"
    assert project["engine"] == 'gc'
    assert project["docs"][0]["sourceLanguageCode"] == 'zh-cn'
    assert project["docs"][1]["sourceLanguageCode"] == 'zh-cn'

@pytest.fixture
def project_config_pro5():
    docs = [
            '2.4 非临床综述.docx',
            '2.6.1 前言.docx',
            '2.6.2 药理学文字总结.docx',
            '2.6.4 药代动力学文字总结.docx',
            '2.6.6 毒理学文字总结.docx',
            'TER-LY03015-PH-007-LPM3770164对大鼠自主活动影响的剂量效应关系研究试验-试验报告.docx',
            'TER-LY03015-PH-008-LPM3770164对大鼠自主活动影响的时间效应关系研究试验-试验报告 .docx',
            'TER-LY03015-PH-009 大鼠催乳素的药效研究.docx',
            'TER-LY03015-PH-010-LPM3770164诱导SD大鼠眼睑下垂的药效研究-试验报告.docx',
            ]
    return generate_project_config("project 5", 'gc', docs, 'zh-cn', 'en', glossary='bt-zh-en-LetPub-glossary')



def project_config_pro4():
    docs = [
            #'XKH001_China PIND (2.4 NC Overview)_For translation use only - Part 2.docx'
            'XKH001_China 2.2 Intro_V1.docx',
            'XKH001_China 2.6.1 Intro_V1.docx',
            'XKH001_China 2.6.2 PD Written Summry_V1.docx',
            'XKH001_China 2.6.4 PK Written Summry_V1.docx',
            'XKH001_China 2.6.5 PK Tabulated Summry_V1.docx',
            'XKH001_China 2.6.6 Tox Written Summary_V1.docx',
            'XKH001_China 2.6.7 Tox tabulated Summary_V1.docx',
            'XKH001_China_2.6.3 PD Tabulated Sum_V1.docx',
#            'XKH001_China PIND (2.4 NC Overview)_For translation use only - Part 2.docx',
#            'XKH001_China PIND (2.4 NC Overview)_For translation use only - Part 2.docx',
            'XKH001_China pre-IND questions_v0.2 JC.docx'
            ]

    return generate_project_config("project 4", 'gc', docs, 'en', 'zh-cn', glossary="")


@pytest.fixture
def project_config_pro3():
    docs = [
            #'2.4 非临床研究概述-LY03009-20210204.docx',
            #'2.6 非临床试验文字和列表总结-LY03009-20210122.docx',
            #'2.6.1 前言-LY03009-20210122.docx',
            #'2.6.2 药理学文字总结-汇总-LY03009-20210122.docx',
            #'2.6.3 药理学列表总结-LY03009-20210122.docx',
            #'2.6.6 毒理学文字总结 -LY03009-20210122.docx',
            '2.6.7 毒理学试验列表-LY03009-20210122.docx'
    ]

    return generate_project_config("project 3", "gc", docs, 'zh-cn', 'en')



@pytest.fixture
def project_config_gc():
    
    project = {
        "name": "demo 01",
        "engine": "gc",
        "docs": [
            {
                "sourceLanguageCode": "zh-cn",
                "targetLanguageCode": "en",
                "file": "NC PD Report Sample.docx",
            },
            #{
            #    "sourceLanguageCode": "en",
            #    "targetLanguageCode": "zh-cn",
            #    "file": "NC Tox Report Sample.docx",
            #},
        ],
    }
    return project

@pytest.fixture
def project_config_pro1():
    project = {
        "name": "demo 01",
        "engine": "aws",
        "docs": [
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
        ],
    }
    return project

@pytest.fixture
def project_config_pro2():
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
    return project

