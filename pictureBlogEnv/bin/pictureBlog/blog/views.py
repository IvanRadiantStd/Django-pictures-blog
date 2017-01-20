# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from blog.models import Post,Opinion
from django.contrib import auth
from django.views.generic.base import View
from django.http import HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def main_page(request):
	page_title = "Блог картинок"
	return render(request, 'main-page_tpl.html', { 'page_title' : page_title, 'userName': auth.get_user(request).username})

class PicturesPage(View):
	model = Post
	context_object_name = 'posts'
	page_title = "Картинки"
    # Название шаблона
	template_name = 'pictures-page_tpl.html'
    # Количество объектов на 1 страницу
	paginate_by = 10
	def get(self, request):
		posts = Post.objects.all()
		return render(request, 'pictures-page_tpl.html', {'posts': posts, 'page_title' : self.page_title, 'userName': auth.get_user(request).username})
	

def about_page(request):
	page_title = "Об авторах"
	return render(request, 'about-page_tpl.html', { 'page_title' : page_title,'userName': auth.get_user(request).username})

def addlike(request, post_id):
	user = auth.get_user(request)
	if(user):
		try:
			post = Post.objects.get(id = post_id)
			try:
				opinion = Opinion.objects.get(opinion_post = post_id, opinion_author = user.id)
				if(opinion.opinion_opn == 1):
					return HttpResponseBadRequest()
				else:
					opinion.opinion_opn = 1
					post.post_dislikes -= 1
					post.save()
					opinion.save()
					likes = post.difference()
			except ObjectDoesNotExist:
				opinion = Opinion(opinion_author = user, opinion_post = post, opinion_opn = 1)
				post.post_likes += 1
				post.save()
				opinion.save()
				likes = post.difference()
		except ObjectDoesNotExist:
			raise HttpResponseBadRequest()
		
		return HttpResponse(likes)
	else:
		return HttpResponseBadRequest()

def dislike(request, post_id):
	user = auth.get_user(request)
	if(user):
		try:
			post = Post.objects.get(id = post_id)
			try:
				opinion = Opinion.objects.get(opinion_post = post_id, opinion_author = user.id)
				if(opinion.opinion_opn == -1):
					return HttpResponseBadRequest()
				else:
					opinion.opinion_opn = -1
					post.post_likes -= 1
					post.save()
					opinion.save()
					likes = post.difference()
			except ObjectDoesNotExist:
				opinion = Opinion(opinion_author = user, opinion_post = post, opinion_opn = -1)
				post.post_dislikes += 1
				post.save()
				opinion.save()
				likes = post.difference()

		except ObjectDoesNotExist:
			raise HttpResponseBadRequest()
		
		return HttpResponse(likes)
	else:
		return HttpResponseBadRequest()