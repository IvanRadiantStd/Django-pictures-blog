# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User
from blog.forms import PostForm
# Create your views here.

@csrf_protect
def login(request):
	args = {}
	if request.POST:
		userName = request.POST.get('Login', '')
		password = request.POST.get('Password', '')
		user = auth.authenticate(username = userName, password = password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			return HttpResponseBadRequest("Ошибка! Пользователь не найден или пароль введён неверно!")
	else:
		return render(request, 'loginSys_tpl.html')



def logout(request):
	auth.logout(request)
	return redirect("/")

@csrf_protect
def register(request):
	args = {}
	if request.POST:
		name = request.POST.get('username')
		password = request.POST.get('password1')
		passwordConfirm = request.POST.get('password2')
		if(password == passwordConfirm):
			user = User.objects.create_user(name, '', password)
			user.save()
		newuser = auth.authenticate(username = name,
										password = password)
		auth.login(request, newuser)
		return redirect('/')
	else:
			return HttpResponseBadRequest(newuser_form)
	return render(request, "register_tpl.html", args)

@csrf_protect
def addPost(request):
	user = auth.get_user(request)
	if(user):
		if request.POST:
			form = PostForm(request.POST, request.FILES)
			if form.is_valid():
				post = form.save(commit = False)
				post.post_author = user
				form.save()
				return redirect('/pictures/')
			else:
				return HttpResponseBadRequest()
		else:
			return HttpResponseBadRequest()
	return redirect('/pictures/')