from tests.common.utils import env
from tests.common.extract_pdf_info import ExtractPDFinfo


MAIN_PATH = env.get('MAIN_PATH')
template_pdf_path = MAIN_PATH + r'\tests\test_task.pdf'

pdf_info_extractor = ExtractPDFinfo(template_pdf_path)

TEMPLATE_TEXT = pdf_info_extractor.extract_template_words()
TEMPLATE_CROPBOX = pdf_info_extractor.get_pdf_page_cropbox()
