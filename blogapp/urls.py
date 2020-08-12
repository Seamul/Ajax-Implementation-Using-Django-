
from django.urls import path

from blogapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('',views.a),
    # path('test',views.f),
    path('create/', views.image_create, name='create'),
    path('index/', views.index, name='index'),
    path('save_book/', views.savebook, name='savebook'),
    path('getAllBook/', views.getAllBook, name='getAllBook'),
    path('deletebook/', views.deletebook, name='deletebook'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)