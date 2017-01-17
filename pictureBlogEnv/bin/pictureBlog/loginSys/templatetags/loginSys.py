# -*- coding: UTF-8 -*-
from django import template
from django.contrib.auth.forms import UserCreationForm
from blog.forms import PostForm

register=template.Library()

@register.inclusion_tag('postAdd_tpl.html') # регистрируем тег и подключаем шаблон 
def postAdd():
	args = {}
	args["form"] = PostForm
	return args
@register.inclusion_tag('register_tpl.html') # регистрируем тег и подключаем шаблон 
def registerSys():
	args = {}
	args["form"] = UserCreationForm()
	return args
@register.inclusion_tag('loginSys_tpl.html') # регистрируем тег и подключаем шаблон 
def loginSys():
	return {}

