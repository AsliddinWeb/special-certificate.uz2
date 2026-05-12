from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Photo, Video


@admin.register(Photo)
class PhotoAdmin(TranslationAdmin):
    list_display = ['title', 'is_active', 'order', 'created_at']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    ordering = ['order', '-created_at']


@admin.register(Video)
class VideoAdmin(TranslationAdmin):
    list_display = ['title', 'is_active', 'order', 'created_at']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    ordering = ['order', '-created_at']