# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import mock

from django.test import TestCase
from .models import PDFFile

# Create your tests here.
class PDFFileUploadTest(TestCase):

    @mock.patch('PyPDF2.PdfFileMerger')
    def test_upload_ok(self, merger_mock):
        with open('core/files/test.pdf', 'rb') as f:
            with self.settings(MEDIA_ROOT='/tmp', PDF_PREVIEWS_ROOT='/tmp'):
                self.client.post('/create', {'name': 'test', 'pdf_file': f})
        self.assertEqual(len(merger_mock.mock_calls), 4)

    def test_upload_fail(self):
        with open('core/files/test.bad', 'r') as bad:
            response = self.client.post('/create', {'name': 'test', 'pdf_file': bad})
        self.assertIn('You can upload only PDF files', response.content)
        

    def test_pdf_name(self):
        pdf_file = PDFFile.objects.create(name='test')
        self.assertEqual(str(pdf_file), 'PDF: test')

