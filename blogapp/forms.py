# from django import forms
# from .models import Post
# class PostModel(forms.ModelForm):
# 	"""docstring for PostModel"""
# 	alu=forms.CharField()
# 	potol=forms.CharField(max_length=499)
# 	class Meta:
# 		model=Post
# 		fields=('title','url')



			

from django import forms

from .models import Image

class ImageCreateForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('title', 'url','img')
        # widgets = {
        #     'url': forms.HiddenInput,
        # }