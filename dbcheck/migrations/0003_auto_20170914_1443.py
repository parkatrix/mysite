# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 05:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dbcheck', '0002_auto_20170914_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='updated_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
