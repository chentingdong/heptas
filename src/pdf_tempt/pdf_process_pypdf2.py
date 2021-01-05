from PyPDF2 import PdfFileReader


class DocumentProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path, "rb") as f:
            pdf = PdfFileReader(f)
            self.information = pdf.getDocumentInfo()
            self.pages = pdf.getPage(1)
            self.content0 = self.pages.getContents()
            self.number_of_pages = pdf.getNumPages()

    def extract_information(self):
        txt = """
            Information about {file_path}
            Author: {author}
            Subject: {title}
            Number of Pages: {pages}
            content 0: {content}
            """.format(
            file_path=self.file_path,
            author=self.information.author,
            title=self.information.title,
            pages=self.number_of_pages,
            content=self.content0,
        )

        print(txt)


if __name__ == "__main__":
    dp = DocumentProcessor(
        "../data/input/coronavirus-covid-19-covid-19-what-you-need-to-know_2.pdf"
    )
    dp.extract_information()
