# -*- coding: UTF-8 -*-
from django import template
from blogNavigation.models import Navigation

register=template.Library()

@register.inclusion_tag('blog-navigation_tpl.html') # регистрируем тег и подключаем шаблон 
def navigation():
	menu_items = Navigation.objects.all()
	return { 'menu_items' : menu_items}

