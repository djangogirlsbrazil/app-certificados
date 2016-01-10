# coding: utf-8
from django import forms
from django.core.exceptions import ValidationError

from .models import Attendees


def validate_file_extension(file):
    if not file.name.endswith('.csv'):
        raise ValidationError(u'É necessário que o arquivo tenha extensão .CSV')


class AttendeesForm(forms.Form):
    uploaded_file = forms.FileField(validators=[validate_file_extension])


class AttendeesCertificationForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            Attendees.objects.get(email=data)
        except Attendees.DoesNotExist:
            raise ValidationError(u'E-mail não cadastrado.')

        return data
