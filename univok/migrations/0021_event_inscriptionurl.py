# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-11 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univok', '0020_event_displayinscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='inscriptionurl',
            field=models.CharField(default='default', max_length=1000),
        ),
    ]
