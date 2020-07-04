from django.contrib import admin
from blog.models import Blog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    class Media:
        # css = { 'all': ('css/fancy.css',)}
        js = ('js/tiny.js',)

admin.site.register(Blog, BlogAdmin)