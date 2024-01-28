from django.contrib import admin
from blog.models import Post 
from blog.models import BlogComment
# Register your models here.

admin.site.register(BlogComment)

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)