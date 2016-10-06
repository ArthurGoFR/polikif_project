# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-05 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gdpcore', '0034_auto_20160923_1310'),
        ('univok', '0016_converter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='converter',
            name='html',
            field=models.CharField(max_length=100000),
        ),
        migrations.RemoveField(
            model_name='sentence',
            name='proposition',
        ),
        migrations.AddField(
            model_name='sentence',
            name='proposition',
            field=models.ManyToManyField(to='gdpcore.Proposition'),
        ),
    ]