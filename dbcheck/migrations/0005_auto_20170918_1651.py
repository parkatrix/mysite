# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbcheck', '0004_auto_20170918_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='ms',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
