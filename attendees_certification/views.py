from django.shortcuts import render
from django.views.generic.edit import FormView

from attendees_certification.forms import AttendeesForm

class AttendeesUploadFormView(FormView):
    form_class = AttendeesForm
    template_name = 'upload.html'
    success_url = '/success/'

    def form_invalid(self, form):
        return super(AttendeesUploadFormView, self).form_valid(form)

    def form_valid(self, form):
        return super(AttendeesUploadFormView, self).form_valid(form)
