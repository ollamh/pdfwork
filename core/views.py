# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.files import File
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import PDFFile
from .forms import PDFForm
from .utils import create_preview 


class PDFCreateView(CreateView):

    model = PDFFile
    form_class = PDFForm

    def form_valid(self, form):
        self.object = form.save()
        preview_file_name = create_preview(self.object)
        self.object.pdf_file_preview = 'previews/{}'.format(preview_file_name)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('pdf:list') 

class PDFListView(ListView):

    model = PDFFile
