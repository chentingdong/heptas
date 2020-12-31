import os
import docx
from googletrans import Translator
from ..logs.logger import translation_logger as logger
from ..configs.config import cfg
from .utils import get_outfile_path


class DocxProcessor:
    def __init__(self, infile_path):
        self.infile_path = infile_path
        self.outfile_path = get_outfile_path(infile_path)
        self.summary_length = cfg["debug"]["summary_length"]
        self.translator = Translator()
        self.error_count = 0
        self.load_doc(infile_path)

    def load_doc(self, file_path):
        logger.info("Loading document...")
        self.doc = docx.Document(file_path)
        self.paragraphs = self.doc.paragraphs

    def translate(self):
        try:
            self.translate_tables()
            self.translate_paragraphs()
            print(self.outfile_path)
            self.doc.save(self.outfile_path)
            logger.info("Translation completed: {}".format(self.outfile_path))
            return True
        except Exception as error:
            logger.error("Translation failed: {}".format(error))
            return False

    def translate_paragraphs(self, start=None, end=None):
        if start is None:
            start = 0
        if end is None:
            end = len(self.paragraphs)

        logger.info("Started translating paragraphs...")
        for i, paragraph in enumerate(self.paragraphs):
            self.translate_paragraph_one(paragraph)
        logger.info("Finished translating paragraphs...")

    def translate_paragraph_one(self, paragraph):
        try:
            inline = paragraph.runs
            for i in range(len(inline)):
                if inline[i].text is None:
                    continue
                translation = self.translator.translate(
                    inline[i].text, src="chinese (simplified)", dest="en"
                )
                inline[i].text = translation.text
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
