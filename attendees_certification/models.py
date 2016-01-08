# -*- coding: utf-8 -*-
from django.db import models


class Attendees(models.Model):

    name = models.CharField(
        u'Nome',
        null=False,
        blank=False,
        max_length=255,
    )
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    birthday = models.DateField(
        u'Data de Nascimento',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
