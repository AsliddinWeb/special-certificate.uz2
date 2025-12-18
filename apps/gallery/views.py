from django.shortcuts import render
from .models import Photo, Video


def gallery_index(request):
    """Asosiy gallery sahifasi - 2 ta card"""
    photo_count = Photo.objects.filter(is_active=True).count()
    video_count = Video.objects.filter(is_active=True).count()

    context = {
        'photo_count': photo_count,
        'video_count': video_count,
    }
    return render(request, 'gallery/index.html', context)


def photo_gallery(request):
    """Foto galereya"""
    photos = Photo.objects.filter(is_active=True)
    return render(request, 'gallery/photos.html', {'photos': photos})


def video_gallery(request):
    """Video galereya"""
    videos = Video.objects.filter(is_active=True)
    return render(request, 'gallery/videos.html', {'videos': videos})