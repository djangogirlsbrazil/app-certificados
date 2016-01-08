# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.views.generic import TemplateView

from .views import AttendeesUploadFormView
from .views import AttendeesGetCertificationFormView
from .views import SuccessCertificationDetailView


urlpatterns = [
    url(r'^upload/$', AttendeesUploadFormView.as_view(), name='file_upload'),
    url(r'^upload/success/$', TemplateView.as_view(template_name='success.html'), name='upload_success'),
    url(r'^certification/$', AttendeesGetCertificationFormView.as_view(), name='get_certification'),
    url(
        regex=r'^certification/success/(?P<pk>[\w.@+-]+)/$',
        view=SuccessCertificationDetailView.as_view(),
        name='certification_success'
    ),

]
