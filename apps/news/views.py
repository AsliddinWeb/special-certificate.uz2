# apps/news/views.py

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, News


def news_list(request):
    """Barcha yangiliklar ro'yxati"""
    news_list = News.objects.filter(is_active=True).select_related('category')
    categories = Category.objects.filter(is_active=True)

    # Kategoriya bo'yicha filter
    category_slug = request.GET.get('category')
    if category_slug:
        news_list = news_list.filter(category__slug=category_slug)

    # Pagination
    paginator = Paginator(news_list, 9)  # 9 ta yangilik per page
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    context = {
        'news': news,
        'categories': categories,
        'current_category': category_slug,
    }
    return render(request, 'news/list.html', context)


def news_detail(request, slug):
    """Yangilik tafsilotlari"""
    news = get_object_or_404(News, slug=slug, is_active=True)

    # Ko'rishlar sonini oshirish
    news.increment_views()

    # O'xshash yangiliklar
    related_news = News.objects.filter(
        is_active=True,
        category=news.category
    ).exclude(pk=news.pk)[:3]

    # Oldingi va keyingi yangilik
    previous_news = News.objects.filter(
        is_active=True,
        created_at__lt=news.created_at
    ).first()

    next_news = News.objects.filter(
        is_active=True,
        created_at__gt=news.created_at
    ).order_by('created_at').first()

    context = {
        'news': news,
        'related_news': related_news,
        'previous_news': previous_news,
        'next_news': next_news,
    }
    return render(request, 'news/detail.html', context)


def news_category(request, slug):
    """Kategoriya bo'yicha yangiliklar"""
    category = get_object_or_404(Category, slug=slug, is_active=True)
    news_list = News.objects.filter(is_active=True, category=category)
    categories = Category.objects.filter(is_active=True)

    # Pagination
    paginator = Paginator(news_list, 9)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    context = {
        'news': news,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'news/list.html', context)