# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 08:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20170120_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extanduser',
            name='extandUser_user',
        ),
        migrations.AlterField(
            model_name='view',
            name='view_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ExtandUser',
        ),
    ]
