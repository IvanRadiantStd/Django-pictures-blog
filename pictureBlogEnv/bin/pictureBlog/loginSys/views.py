# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.http import HttpResponseBadRequest
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