# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendees_certification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendees',
            name='birthday',
            field=models.DateField(verbose_name='Data de Nascimento', null=True, blank=True),
        ),
    ]
