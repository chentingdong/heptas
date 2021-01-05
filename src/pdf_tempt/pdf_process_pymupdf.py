import fitz


class DocumentProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.pdf = fitz.open(file_path)

    def display_page(self, page_number=0):
        page = self.pdf.loadPage(page_number)
        page1text = page.getText("text")
        print(page1text)


if __name__ == "__main__":
    dp = DocumentProcessor(
        "../data/input/coronavirus-covid-19-covid-19-what-you-need-to-know_2.pdf"
    )
    dp.display_page(1)
