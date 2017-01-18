# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20170116_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_description',
            field=models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
    ]