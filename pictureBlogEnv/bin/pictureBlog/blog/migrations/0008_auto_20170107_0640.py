# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_like',
            field=models.IntegerField(default=0),
        ),
    ]