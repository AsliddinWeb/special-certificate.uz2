from modeltranslation.translator import register, TranslationOptions

from .models import Photo, Video


@register(Photo)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
