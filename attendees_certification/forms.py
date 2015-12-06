# coding: utf-8
from django import forms
from django.core.exceptions import ValidationError


def validate_file_extension(file):
    if not file.name.endswith('.csv'):
        raise ValidationError(u'O formato precisa ser .CSV')


class AttendeesForm(forms.Form):
    uploaded_file = forms.FileField(label=u'Arquivo CSV', validators=[validate_file_extension])
