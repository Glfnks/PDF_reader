from tests.common.constants import MAIN_PATH
from tests.common.constants import TEMPLATE_CROPBOX
from tests.common.extract_pdf_info import ExtractPDFinfo
from tests.common.compare_dpf_data import ComparePDFdata


test_pdf_path = MAIN_PATH + r'\tests\test_failed.pdf'


def compare_pdf(target_pdf_path):
    target_pdf_info = ExtractPDFinfo(target_pdf_path)

    template_cropbox = TEMPLATE_CROPBOX
    target_cropbox = target_pdf_info.get_pdf_page_cropbox()

    ComparePDFdata.compare_template_text_in_pdf(target_pdf_path)
    ComparePDFdata.compare_cropbox_from_two_pages(template_cropbox, target_cropbox)


if __name__ == '__main__':
    compare_pdf(test_pdf_path)
