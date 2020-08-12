from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from rest_framework import serializers

class Image(models.Model):
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True)
    url = models.URLField()
    img=models.ImageField(upload_to='images/%y/%m/%d')
    created=models.DateField(auto_now_add=True)
class Book(models.Model):
	name=models.CharField(max_length=80)
	prize=models.IntegerField()
	pages=models.IntegerField()

class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=80)
    prize = serializers.IntegerField()
    pages = serializers.IntegerField()
    id = serializers.IntegerField()