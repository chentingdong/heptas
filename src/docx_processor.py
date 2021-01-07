import os
import docx
import json
from .logger import translation_logger as logger
from .translator import Translator
from ..configs.config import cfg, get_infile_path, get_outfile_path


class DocxProcessor:
    def __init__(self, infile=None, engine=None):
        self.outfile_path = get_outfile_path(infile, engine)
        self.summary_length = cfg["debug"]["summary_length"]
        self.error_count = 0
        self.engine = engine
        self.translator = Translator(engine=engine)
        if engine is None:
            self.engine = cfg["translate"]["engine"]
        self.load_doc(infile)

    def load_doc(self, infile):
        logger.info("Loading document...")
        infile_path = get_infile_path(infile)
        self.infile_path = infile_path
        self.doc = docx.Document(infile_path)
        self.paragraphs = self.doc.paragraphs

    def set_style(self):
        self.doc.styles["Normal"].font.name = "Times"

    def translate_doc(self):
        try:
            self.set_style()
            self.translate_tables()
            self.translate_paragraphs()
            print(self.outfile_path)
            self.doc.save(self.outfile_path)
            logger.info("Translation completed: {}".format(self.outfile_path))
            return True
        except Exception as error:
            logger.error("Translation failed: {}".format(error))
            return False

    def translate_paragraphs(self):
        logger.info("Started translating paragraphs...")
        for paragraph in self.paragraphs:
            self.translate_paragraph_one(paragraph)
        logger.info("Finished translating paragraphs...")

    def translate_paragraph_one(self, paragraph):
        try:
            if paragraph.text != "":
                paragraph.text = self.translator.translate(paragraph.text)
        except Exception as error:
            self.error_count += 1
            summary = paragraph.text[: self.summary_length] + "..."
            logger.error("{}: {}\n{}".format(self.error_count, error, summary))

    def translate_tables(self):
        logger.info("Started translating tables...")
        for table in self.doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for paragraph in cell.paragraphs:
                        self.translate_paragraph_one(paragraph)
        logger.info("Finished translating tables...")
