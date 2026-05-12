from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = "Special Certificate"
admin.site.site_header = "Special Certificate Admin"
admin.site.index_title = "Boshqaruv paneli"

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),

    # Bosh sahifa
    path('', include('apps.core.urls')),

    # Servislar
    path('services/', include('apps.services.urls')),

    # Galereya
    path('gallery/', include('apps.gallery.urls')),

    # Yangiliklar
    path('news/', include('apps.news.urls')),

    prefix_default_language=True,
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
