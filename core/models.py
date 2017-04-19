# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .validators import validate_file_extension


class PDFFile(models.Model):

    name = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='uploads/', validators=[validate_file_extension])
    pdf_file_preview = models.FileField(upload_to='previews/', null=True)

    def __str__(self):
        return 'PDF: {}'.format(self.name)

