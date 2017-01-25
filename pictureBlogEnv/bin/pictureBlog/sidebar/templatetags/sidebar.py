# -*- coding: UTF-8 -*-
from django import template
from blog.models import Post, Tag

register=template.Library()

@register.inclusion_tag('sidebar_tpl.html') # регистрируем тег и подключаем шаблон 
def sidebar():
	args = {}
	args['posts_last'] = Post.objects.raw("SELECT * FROM post WHERE post_date >= (now() - '1 HOUR'::interval)")
	args['posts_best'] = Post.objects.raw('SELECT * FROM post WHERE (post_likes-post_dislikes) > (SELECT (SUM(post_likes-post_dislikes)/COUNT(*)) FROM post)')
	args['tags'] = Tag.objects.all()
	return args