import pdfplumber
from pdfminer.layout import LTTextContainer
from pdfminer.high_level import extract_pages


class ExtractPDFinfo:
    """
    Common methods to get info from PFD file
    """

    def __init__(self, pdf_path):
        self._pdf_path = pdf_path

    def get_pdf_data(self) -> dict:
        """
        Extract text in PDF file
        :return: dict
        """
        data = {}

        with pdfplumber.open(self._pdf_path) as pdf:
            page = pdf.pages[0]
            text = page.extract_text()

            data['data'] = text

        return data

    def extract_template_words(self) -> list:
        """
            Extract main words from the template PDF file
        :return: list
        """
        text_with_styles = []

        for page_layout in extract_pages(self._pdf_path):
            for element in page_layout:
                if isinstance(element, LTTextContainer):
                    for text_line in element:
                        text_with_styles.append(text_line.get_text().split(':')[0].strip().replace('\n', ''))

        while '' in text_with_styles:
            text_with_styles.remove('')

        return text_with_styles

    def get_pdf_page_cropbox(self) -> tuple:
        """
            Get cropbox value from PDF file
        :return: tuple
        """
        with pdfplumber.open(self._pdf_path) as template_pdf:
            pdf_page = template_pdf.pages[0]

        _cropbox = pdf_page.cropbox if pdf_page.cropbox else (
            0, 0, pdf_page.width, pdf_page.height)

        return _cropbox
