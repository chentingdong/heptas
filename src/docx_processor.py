import docx
from googletrans import Translator
from ..logs.logger import translation_logger as logger
from ..configs.config import cfg


class DocxProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.target_path = "../data/output"
        self.translator = Translator()
        self.error_count = 0
        self.load_doc(file_path)

    def load_doc(self, file_path):
        logger.info("Loading document...")
        self.doc = docx.Document(file_path)
        self.paragraphs = self.doc.paragraphs

    def translate(self, output_path=None):
        try:
            self.translate_tables()
            self.translate_paragraphs()
            self.doc.save(output_path)
            logger.info("Document translation is completed.")
            return True
        except:
            return False

    def translate_paragraphs(self, start=None, end=None):
        if start is None:
            start = 0
        if end is None:
            end = len(self.paragraphs)

        logger.info("Started translating paragraphs...")
        for i, paragraph in enumerate(self.paragraphs):
            self.translate_paragraph_one(paragraph)

    def translate_paragraph_one(self, paragraph):
        try:
            inline = paragraph.runs

            for i in range(len(inline)):
                translation = self.translator.translate(
                    inline[i].text, src="chinese (simplified)", dest="en"
                )
                inline[i].text = translation.text
            logger.debug("Finished translating paragraph {}".format(i))
        except Exception as error:
            self.error_count += 1
            logger.error(
                "{error_count}: {error}\n{partial}".format(
                    error_count=self.error_count,
                    error=error,
                    partial=paragraph.text[: cfg.get("summary_length", 100)],
                )
            )

    def translate_tables(self):
        logger.info("Started translating tables...")

        for table in self.doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for paragraph in cell.paragraphs:
                        self.translate_paragraph_one(paragraph)
        logger.info("Started translating tables...")
