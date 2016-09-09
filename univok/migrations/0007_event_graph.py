# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-06 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gdpcore', '0031_auto_20160617_1206'),
        ('univok', '0006_auto_20160906_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='graph',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gdpcore.Graph'),
            preserve_default=False,
        ),
    ]