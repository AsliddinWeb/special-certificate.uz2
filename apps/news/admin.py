# apps/news/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import Category, News


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'news_count', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order', 'name']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_preview', 'is_active', 'is_featured', 'views', 'created_at']
    list_editable = ['is_active', 'is_featured']
    list_filter = ['is_active', 'is_featured', 'category', 'created_at']
    search_fields = ['title', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

    fieldsets = (
        ('Asosiy', {
            'fields': ('title', 'slug', 'category', 'image')
        }),
        ('Kontent', {
            'fields': ('excerpt', 'content')
        }),
        ('Sozlamalar', {
            'fields': ('is_active', 'is_featured'),
            'classes': ('collapse',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 8px;" />',
                               obj.image.url)
        return "-"

    image_preview.short_description = "Rasm"