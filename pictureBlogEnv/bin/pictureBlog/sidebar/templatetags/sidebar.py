# -*- coding: UTF-8 -*-
from django import template
from blog.models import Post

register=template.Library()

@register.inclusion_tag('sidebar_tpl.html') # регистрируем тег и подключаем шаблон 
def sidebar():
	posts = Post.objects.all()
	return { 'posts' : posts}