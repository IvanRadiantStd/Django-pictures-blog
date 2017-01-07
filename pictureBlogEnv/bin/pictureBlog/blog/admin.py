from django.contrib import admin
from blog.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	fields = ['post_title','post_description','post_date', 'post_img']

admin.site.register(Post,PostAdmin);