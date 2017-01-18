# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from blog.models import Post
from django.contrib import auth
# Create your views here.

def main_page(request):
	page_title = "Блог картинок"
	return render(request, 'main-page_tpl.html', { 'page_title' : page_title, 'userName': auth.get_user(request).username})

def pictures_page(request):
	page_title = "Картинки"
	posts = Post.objects.all()
	return render(request, 'pictures-page_tpl.html', {'posts': posts, 'page_title' : page_title, 'userName': auth.get_user(request).username})


def about_page(request):
	page_title = "Об авторах"
	return render(request, 'about-page_tpl.html', { 'page_title' : page_title,'userName': auth.get_user(request).username})