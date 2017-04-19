from __future__ import unicode_literals

from django.forms import ValidationError

def validate_file_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('You can upload only PDF files')
