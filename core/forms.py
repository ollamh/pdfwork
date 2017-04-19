from __future__ import unicode_literals, print_function

from django import forms
from .models import PDFFile

class PDFForm(forms.ModelForm):

    class Meta:
        model = PDFFile
        fields = ['name', 'pdf_file']

