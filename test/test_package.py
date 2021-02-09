from docx.opc.package import OpcPackage, Unmarshaller
from docx.package import Package
from docx.parts.document import DocumentPart
from docx import Document
from docx.oxml import parse_xml, OxmlElement
from lxml import etree


CONTENT_NAMESPACE = "{http://schemas.openxmlformats.org/package/2006/content-types}"
WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
MARKUP_COMPATIBILITY = '{http://schemas.openxmlformats.org/markup-compatibility/2006}'
SCM = '{urn:schemas-microsoft-com:vml}'
PARAGRAPH = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'
STYLE = WORD_NAMESPACE + 'pStyle'
TABLE = WORD_NAMESPACE + 'tbl'
ROW   = WORD_NAMESPACE + 'tr'
CELL  = WORD_NAMESPACE + 'tc'
CONTENT = WORD_NAMESPACE + 'r'
ALTERNATE_CONTENT = MARKUP_COMPATIBILITY + 'AlternateContent'
TEXTBOX = SCM + 'textbox'
TEXTBOX_CONTENT = WORD_NAMESPACE + 'txbxContent'

doc = "../data/input/CMC test 5-SHARK细胞培养工艺描述 30116-R2.docx"
doc_out = "../data/input/CMC test 5-SHARK细胞培养工艺描述 30116-R2.tb.docx"

p = Package.open(doc)

# different files in word package
#for part in p.iter_parts():
#    print(part.partname + "\n");

# explore Document
docx = Document(doc)
counter = 0
for para in docx.paragraphs:
    counter += 1
    element = para._element
    #print(element.tag)
    for name in element.iter(TEXTBOX_CONTENT):
        for p in name.iter(PARAGRAPH):
            for r in p.iter(CONTENT):
                for t in r.iter(TEXT):
                    #print(t.text)
                    t.text = 'TTTESTTTT'
        #print(name.xpath("//text()"))
        #print(etree.tostring(name, method='TEXT'));
docx.save(doc_out);

exit
for para in docx.paragraphs:
    counter += 1
    if counter == 3:
        #print(para._element.xml)
        element = para._element
        print(len(element))
        print(element.tag)
        #print(element.find(CONTENT))
        if element.find(CONTENT):
            for child in element:
                print(child.tag)
                if child.find(ALTERNATE_CONTENT):
                    for c in child:
                        print(c.tag)
                #print(child.xml)
                #print(etree.tostring(child, method='text'))
                #print(child.xpath("//text()"))
        #element.find("<w:r>")
        #print(para._element)
        #break
#print(parse_xml(docx.l))

#print(docx.part.blob)
