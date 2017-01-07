from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from blog.models import Post
# Create your views here.

def blog(request):
	return render_to_response('sidebar.html', {'posts' : Post.objects.all()})