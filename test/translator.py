from ..src.translator import Translator


def test_translator():
    text = "雷曼兄弟公司的倒闭和柏林墙的倒塌没有任何关系"
    translator = Translator("../data/model/zh-en/20201120")
    result = translator.translate(text)
    assert (
        result
        == "The collapse of Lehman Brothers has nothing to do with the fall of the Berlin Wall"
    )

# google cloud test
def test_translator_GC():
    text = "雷曼兄弟公司的倒闭和柏林墙的倒塌没有任何关系"
    translator = Translator(engine="gc")
    result = translator.translate(text)
    
    assert (
        result
        == "The collapse of Lehman Brothers has nothing to do with the fall of the Berlin Wall"
    )


