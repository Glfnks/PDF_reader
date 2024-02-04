import pdfplumber

from tests.common.constants import TEMPLATE_TEXT


class ComparePDFdata:
    """
    Compare different data between two pdf files
    """

    @staticmethod
    def compare_cropbox_from_two_pages(template_cropbox: tuple, target_cropbox: tuple, tolerance=0.5) -> None:
        """
            Compare cropbox data between two PDF files
        :param template_cropbox: template pdf data layout
        :param target_cropbox: target pdf data layout
        :param tolerance: acceptable margin error
        :return: None
        """
        if not (
                abs(template_cropbox[0] - target_cropbox[0]) <= tolerance and
                abs(template_cropbox[1] - target_cropbox[1]) <= tolerance and
                abs(template_cropbox[2] - target_cropbox[2]) <= tolerance and
                abs(template_cropbox[3] - target_cropbox[3]) <= tolerance
        ):
            raise Exception('Target cropbox is not equal template')

    @staticmethod
    def compare_template_text_in_pdf(target_pdf_path) -> None:
        """
            Compare text in target PDF file with template
        :param target_pdf_path: path to target pdf file
        :return: None
        """

        template_text = TEMPLATE_TEXT

        with pdfplumber.open(target_pdf_path) as target_pdf:
            target_text = target_pdf.pages[0].extract_text()

        for template_block in template_text:
            if template_block not in target_text:
                raise Exception(f'"{template_block}" is absent')
