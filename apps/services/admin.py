from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Service


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title', 'short_description']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['order']