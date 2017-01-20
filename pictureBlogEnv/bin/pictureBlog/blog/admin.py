from django.contrib import admin
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	fields = ['post_title','post_description','post_date', 'post_img', 'post_author']
	list_filter = ['post_date', 'post_author']
	list_display = ['post_title', 'post_date', 'post_author']

class UserAdmin(admin.ModelAdmin):
	list_display = ['username']


admin.site.register(Post,PostAdmin);
admin.site.register(User,UserAdmin);
