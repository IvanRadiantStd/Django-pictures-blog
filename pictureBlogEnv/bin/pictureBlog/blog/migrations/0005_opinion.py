# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-05 23:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion_opn', models.IntegerField(default=-1)),
                ('opinion_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.ExtandUser')),
                ('opinion_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
            options={
                'db_table': 'opinion',
            },
        ),
    ]
