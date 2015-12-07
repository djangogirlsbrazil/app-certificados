# -*- coding: utf-8 -*-
import csv
from django.shortcuts import render
from django.views.generic import FormView, DetailView
from django.core.urlresolvers import reverse_lazy, reverse

from braces.views import LoginRequiredMixin

from .forms import AttendeesForm
from .forms import AttendeesCertificationForm
from .models import Attendees


class AttendeesUploadFormView(LoginRequiredMixin, FormView):
    form_class = AttendeesForm
    template_name = 'upload.html'
    success_url = reverse_lazy('upload_success')
    login_url = '/admin/login'

    def form_invalid(self, form):
        return super(AttendeesUploadFormView, self).form_invalid(form)

    def form_valid(self, form):
        csv_file = self.request.FILES['uploaded_file']
        self.handle_uploaded_file(csv_file)
        return super(AttendeesUploadFormView, self).form_valid(form)

    def handle_uploaded_file(self, file):
        with open(file.temporary_file_path(), 'r') as csv_file:
            girls_csv = csv.reader(csv_file, delimiter=';')
            i = 0
            for row in girls_csv:
                if i == 0:
                    i += 1
                    continue

                name = row[0]
                email = row[1]
                attendees = Attendees(name=name, email=email)
                attendees.save()


class AttendeesGetCertificationFormView(FormView):
    form_class = AttendeesCertificationForm
    template_name = 'certification.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        self.attendee = Attendees.objects.get(email=email)
        self.success_url = reverse('certification_success', kwargs={'pk': self.attendee.pk})
        return super(AttendeesGetCertificationFormView, self).form_valid(form)


class SuccessCertificationDetailView(DetailView):
    template_name = 'certification_success.html'
    model = Attendees
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
