# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import FormView

from braces.views import LoginRequiredMixin

from .forms import AttendeesForm


class AttendeesUploadFormView(LoginRequiredMixin, FormView):
    form_class = AttendeesForm
    template_name = 'upload.html'
    success_url = '/admin/'
    login_url = '/admin/login'

    def form_invalid(self, form):
        # import ipdb; ipdb.set_trace()
        return super(AttendeesUploadFormView, self).form_invalid(form)

    def form_valid(self, form):
        # import ipdb; ipdb.set_trace()
        csv_file = self.get_form()
        return super(AttendeesUploadFormView, self).form_valid(form)

