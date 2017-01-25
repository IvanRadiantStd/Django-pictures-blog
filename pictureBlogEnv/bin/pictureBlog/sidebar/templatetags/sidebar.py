# -*- coding: UTF-8 -*-
from django import template
from blog.models import Post, Tag

register=template.Library()

@register.inclusion_tag('sidebar_tpl.html') # регистрируем тег и подключаем шаблон 
def sidebar():
	args = {}
	args['posts'] = Post.objects.all()
	args['tags'] = Tag.objects.all()
	return args