from django.contrib import admin
from blogNavigation.models import Navigation
# Register your models here.
class NavigationAdmin(admin.ModelAdmin):
	fields = ['navigation_url','navigation_title']
	list_filter = ['navigation_title']
	list_display = ['navigation_title']

admin.site.register(Navigation, NavigationAdmin);