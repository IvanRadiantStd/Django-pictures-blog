# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navigation_url', models.CharField(max_length=200)),
                ('navigation_title', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'navigation',
            },
        ),
    ]
