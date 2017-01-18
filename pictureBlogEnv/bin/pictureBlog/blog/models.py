# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
"""
extended user model to set relations with others entities
"""
class ExtandUser(models.Model):
	class Meta():
		db_table = "extanduser"
	extandUser_user = models.OneToOneField(User,on_delete = models.CASCADE)
	extandUser_email = models.CharField(max_length = 200)

class Post(models.Model):
	class Meta():
		db_table = "post"
	post_title = models.CharField(max_length = 200, verbose_name = 'Название')
	post_img = models.FileField(null = True,  upload_to ="images/",verbose_name = 'Изображение')
	post_description = models.TextField(verbose_name = 'Описание')
	post_date = models.DateTimeField(default = datetime.now)
	post_author = models.ForeignKey(User,blank=True, null= True)
	post_likes = models.IntegerField(default = 0)
	post_dislikes = models.IntegerField(default = 0)
	def difference(self):
		return self.post_likes - self.post_dislikes

class View(models.Model):
	class Meta():
		db_table = "view"
	view_time = models.DateTimeField()
	view_user = models.OneToOneField(ExtandUser, on_delete = models.CASCADE)
	post_view = models.ForeignKey(Post,blank=True, null= True) 

class Opinion(models.Model):
	class Meta():
		db_table = "opinion"
	opinion_opn = models.IntegerField(default = -1)
	opinion_author = models.ForeignKey(ExtandUser,blank=True, null= True)
	opinion_post = models.ForeignKey(Post,blank=True, null= True) 

