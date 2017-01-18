from django.contrib import admin
from blog.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	fields = ['post_title','post_description','post_date', 'post_img', 'post_author']
	list_filter = ['post_date', 'post_author']
	list_display = ['post_title', 'post_date', 'post_author']

admin.site.register(Post,PostAdmin);