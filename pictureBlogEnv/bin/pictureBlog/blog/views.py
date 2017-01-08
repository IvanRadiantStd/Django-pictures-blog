from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from blog.models import Post
from django.contrib import auth
# Create your views here.

def main_page(request):
	return render(request, 'main-page_tpl.html', { 'userName': auth.get_user(request).username})