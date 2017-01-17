# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Navigation(models.Model):
	class Meta():
		db_table = "navigation"
		verbose_name = "Пункт меню"
		verbose_name_plural = "Пункты меню"
	navigation_url = models.CharField(max_length = 200, blank = True)
	navigation_title = models.CharField(max_length = 200)	