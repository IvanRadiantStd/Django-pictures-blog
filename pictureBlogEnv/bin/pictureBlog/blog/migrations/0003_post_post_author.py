# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-05 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170105_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.ExtandUser'),
        ),
    ]
