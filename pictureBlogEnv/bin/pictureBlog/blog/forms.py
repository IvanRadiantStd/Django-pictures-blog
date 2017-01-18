# -*- coding: utf-8 -*-
from django.forms import ModelForm
from models import Post

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['post_img', 'post_title', 'post_description']
