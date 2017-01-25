# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from blog.models import Post,Opinion, Tag
from django.contrib import auth
from django.views.generic.base import View
from django.http import HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
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
	paginate_by = 9
	def get(self, request, page_number = 1, filter = 'all'):
		args = {}
		args['page_title'] = self.page_title
		args['userName'] = auth.get_user(request).username
		all_posts = Post.objects.all()
		current_page = Paginator(all_posts, self.paginate_by)
		args['posts'] = current_page.page(page_number)
		return render(request, self.template_name, args)

def pictures_by_tag(request, tag_id = 1, ):
	paginate_by = 9
	tag = Tag.objects.get(id = tag_id)
	args = {}
	args['page_title'] = tag.tag_title
	args['userName'] = auth.get_user(request).username
	sought_posts = tag.tag_posts.all()
	#current_page = Paginator(sought_posts, paginate_by)
	#args['posts'] = current_page.page(page_number)
	args['posts'] = sought_posts
	return render(request, 'pictures-page_tpl.html', args)

def picturesBest(request):
	paginate_by = 9
	args = {}
	args['page_title'] = 'Лучшие картинки'
	args['userName'] = auth.get_user(request).username
	best_posts = Post.objects.raw('SELECT * FROM post WHERE (post_likes-post_dislikes) > (SELECT (SUM(post_likes-post_dislikes)/COUNT(*)) FROM post)')
	#current_page = Paginator(sought_posts, paginate_by)
	#args['posts'] = current_page.page(page_number)
	args['posts'] = best_posts
	return render(request, 'pictures-page_tpl.html', args)

def picturesLast(request):
	paginate_by = 9
	args = {}
	args['page_title'] = 'За последний час'
	args['userName'] = auth.get_user(request).username
	last_posts = Post.objects.raw("SELECT * FROM post WHERE post_date >= (now() - '1 HOUR'::interval)")
	#current_page = Paginator(sought_posts, paginate_by)
	#args['posts'] = current_page.page(page_number)
	args['posts'] = last_posts
	return render(request, 'pictures-page_tpl.html', args)

def about_page(request):
	args = {}
	args['page_title'] = "Об авторах"
	args['userName'] = auth.get_user(request).username
	return render(request, 'about-page_tpl.html', args)

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