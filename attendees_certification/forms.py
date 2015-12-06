# coding: utf-8
from django import forms


class AttendeesForm(forms.Form):
    uploaded_file = forms.FileField(label=u'Arquivo CSV')
