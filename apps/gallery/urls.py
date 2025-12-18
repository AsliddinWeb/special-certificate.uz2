from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_index, name='index'),
    path('photos/', views.photo_gallery, name='photos'),
    path('videos/', views.video_gallery, name='videos'),
]
