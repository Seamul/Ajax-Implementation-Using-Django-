# from django.shortcuts import render,HttpResponse
# from .forms import PostModel
# from .models import Post
# # Create your views here.
# def a(request):
# 	#return HttpResponse("<h1>seam</h1>")
# 	return render(request,"index.html")
# def f(request):
# 	ob=Post.objects.all()
# 	if request.method=="POST":
# 		form=PostModel(request.POST)
# 		if form.is_valid():
# 			cd=form.cleaned_data
# 			form.save()
# 	else:
# 		form=PostModel(data=request.GET)
# 	return render(request,'test.html',{'form':form,'ob':ob})


	
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image,Book,BookSerializer
import json

def image_create(request):
    form = ImageCreateForm(data=request.POST,files=request.FILES)
    images=Image.objects.all()
    # print(request.FILES)
    if request.method == 'POST':
        # form is sent
        
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            form.save()

            # redirect to new created item detail view
            # return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET 
        form = ImageCreateForm(data=request.GET)

    return render(request,
                  'test.html',
                  {'images': 'images',
                   'form': form})

def index(request):
    return render(request,'index.html')
def savebook(request):
    name=request.GET['name']
    prize=request.GET['prize']
    pages= request.GET['pages']
    book=Book(name=name,prize=prize,pages=pages)
    try:
        book.save()
        return HttpResponse("True")
    except Exception as e:
        return HttpResponse("False")
def getAllBook(request):
    l=list()
    books=Book.objects.all()
    # json formet toiri korlar jjonno  Serializer bebohar kora hoyeche
    # akane akadhik objects ache bole sob guloke age list a rakha hoyeche
    # kintu list theke json a kichu pass kora jaayna bole abar dumps function bebohar kore setake json formet a convert kora hoiche
    for i in books:
        ser=BookSerializer(i)
        l.append(ser.data) 
        print(ser.data)
    print(l)
    return HttpResponse(json.dumps(l))
      
def deletebook(request):
    try:
        print(request.GET['id'])
        books=Book.objects.get(id=request.GET['id'])
        books.delete()
        return HttpResponse("true")
    except Exception as e:
        return HttpResponse("false")

