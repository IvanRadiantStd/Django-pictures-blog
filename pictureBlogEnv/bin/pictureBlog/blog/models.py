from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
extended user model to set relations with others entities
"""
class ExtandUser(models.Model):
	class Meta():
		db_table = "extanduser"
	extandUser_user = models.OneToOneField(User,on_delete = models.CASCADE)

class Post(models.Model):
	class Meta():
		db_table = "post"
	post_title = models.CharField(max_length = 200)
	post_description = models.TextField()
	post_date = models.DateTimeField()
	post_author = models.ForeignKey(ExtandUser,blank=True, null= True)
	post_like = models.IntegerField(default = -1)
	post_dislike = models.IntegerField(default = -1)

class View(models.Model):
	class Meta():
		db_table = "view"
	view_time = models.DateTimeField()
	view_user = models.OneToOneField(ExtandUser)
	post_view = models.ForeignKey(Post,blank=True, null= True) 

class Opinion(models.Model):
	class Meta():
		db_table = "opinion"
	opinion_opn = models.IntegerField(default = -1)
	opinion_author = models.ForeignKey(ExtandUser,blank=True, null= True)
	opinion_post = models.ForeignKey(Post,blank=True, null= True) 