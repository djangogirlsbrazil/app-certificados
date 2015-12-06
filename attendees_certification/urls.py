# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.views.generic import TemplateView

from .views import AttendeesUploadFormView


urlpatterns = [
    url(r'^upload/$', AttendeesUploadFormView.as_view(), name='file_upload'),
    url(r'^upload/success/$', TemplateView.as_view(template_name='success.html'), name='upload_success'),

]
