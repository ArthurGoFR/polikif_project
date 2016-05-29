# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-25 08:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gdpcore', '0018_auto_20160525_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gdpcore.LinkType'),
            preserve_default=False,
        ),
    ]
