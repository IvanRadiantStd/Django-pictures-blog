"""pictureBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^pictures/$', views.PicturesPage.as_view()),
    url(r'^addlike/(?P<post_id>\d+)/$', views.addlike),
    url(r'^dislike/(?P<post_id>\d+)/$', views.dislike),
    url(r'^about/$', views.about_page),
    url(r'^pictures/page/(\d+)/$', views.PicturesPage.as_view()),
    url(r'^$', views.main_page),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)