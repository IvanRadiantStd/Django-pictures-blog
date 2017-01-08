# -*- coding: UTF-8 -*-
from django import template

register=template.Library()

@register.inclusion_tag('loginSys_tpl.html') # регистрируем тег и подключаем шаблон 
def loginSys():
	return {}