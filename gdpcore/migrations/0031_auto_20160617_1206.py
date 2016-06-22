# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-17 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gdpcore', '0030_show_showpart'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='audio'),
        ),
        migrations.AlterField(
            model_name='graph',
            name='parti',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polikif.Parti'),
        ),
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]