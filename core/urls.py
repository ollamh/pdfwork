from django.conf.urls import url

from .views import PDFCreateView, PDFListView

urlpatterns = [
    url(r'^create$', PDFCreateView.as_view(), name='create'),
    url(r'^$', PDFListView.as_view(), name='list')
]
