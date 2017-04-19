# encoding: utf-8
from __future__ import unicode_literals

import os
import PyPDF2

from django.conf import settings

def create_preview(pdf_file):
    file_name, file_ext = os.path.basename(pdf_file.pdf_file.path).rsplit('.', 1)
    preview_file_name = '{}_preview.{}'.format(file_name, file_ext)
    preview_file_path = os.path.join(settings.PDF_PREVIEWS_ROOT, preview_file_name)
    with open(pdf_file.pdf_file.path, 'rb') as main_pdf:
        with open(settings.PDF_PREVIEW_PAGE_PATH, 'rb') as insert_pdf:
            merger = PyPDF2.PdfFileMerger()
            merger.merge(position=0, fileobj=main_pdf, pages=(0, settings.PDF_PREVIEW_CUT_NUMBER))
            merger.merge(position=3, fileobj=insert_pdf)
            merger.write(open(preview_file_path, 'wb'))
    return preview_file_name



