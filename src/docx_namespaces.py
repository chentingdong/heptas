CONTENT_NAMESPACE = "{http://schemas.openxmlformats.org/package/2006/content-types}"
WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
MARKUP_COMPATIBILITY = '{http://schemas.openxmlformats.org/markup-compatibility/2006}'
SCM_NAMESPACE = '{urn:schemas-microsoft-com:vml}'
MATH_NAMESPACE = '{http://schemas.openxmlformats.org/officeDocument/2006/math}'

# TODO: find math 
DOCX_NAMESPACES = {
    "PARAGRAPH" : WORD_NAMESPACE + 'p',
    "TEXT" : WORD_NAMESPACE + 't',
    "STYLE" : WORD_NAMESPACE + 'pStyle',
    "TABLE" : WORD_NAMESPACE + 'tbl',
    "ROW"   : WORD_NAMESPACE + 'tr',
    "CELL"  : WORD_NAMESPACE + 'tc',
    "RUN" : WORD_NAMESPACE + 'r',
    "ALTERNATE_CONTENT" : MARKUP_COMPATIBILITY + 'AlternateContent',
    "TEXTBOX" : SCM_NAMESPACE + 'textbox',
    "TEXTBOX_CONTENT" : WORD_NAMESPACE + 'txbxContent',
    "HYPERLINK" : WORD_NAMESPACE + 'hyperlink',
    # Math related elements
    "OMATHPARA" : MATH_NAMESPACE + 'oMathPara',
    "OMATH" : MATH_NAMESPACE + 'oMath',
    "MATHRUN" : MATH_NAMESPACE + 'r',
    "MATHTEXT" : MATH_NAMESPACE + 't',
    "MATHFRACTION" : MATH_NAMESPACE + 'f',
    "MATHDENOMINATOR" : MATH_NAMESPACE + 'den',
    "MATHNUMERATOR" : MATH_NAMESPACE + 'num',
    }
