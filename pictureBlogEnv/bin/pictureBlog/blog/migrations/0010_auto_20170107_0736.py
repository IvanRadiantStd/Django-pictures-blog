# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170107_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_dislikes',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_likes',
            field=models.IntegerField(default=2),
        ),
    ]