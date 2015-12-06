# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import FormView
import csv

from braces.views import LoginRequiredMixin

from .forms import AttendeesForm
from .models import Attendees

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
                attendees = Attendees(name = name, email = email)
                attendees.save()
                # print(name, email)
