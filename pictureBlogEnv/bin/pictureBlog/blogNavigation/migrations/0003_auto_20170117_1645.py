# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogNavigation', '0002_auto_20170117_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigation',
            name='navigation_title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]