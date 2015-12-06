# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.edit import FormView

from braces.views import LoginRequiredMixin

from .forms import AttendeesForm


class AttendeesUploadFormView(LoginRequiredMixin, FormView):
    form_class = AttendeesForm
    template_name = 'upload.html'
    success_url = '/success/'
    login_url = '/admin/login'

    def form_invalid(self, form):
        return super(AttendeesUploadFormView, self).form_valid(form)

    def form_valid(self, form):
        return super(AttendeesUploadFormView, self).form_valid(form)
