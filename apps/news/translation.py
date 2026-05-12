from modeltranslation.translator import register, TranslationOptions

from .models import Category, News


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'excerpt', 'content')
