# from django.contrib import admin

# # Register your models here.


# # Register your models here.
# from .models import Post
# @admin.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'author', 'publish')
#     

from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
