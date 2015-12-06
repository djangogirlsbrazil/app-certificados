# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from .views import AttendeesUploadFormView


urlpatterns = [
    url(r'^upload/', AttendeesUploadFormView.as_view()),
]
