from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = "Special Certificate"
admin.site.site_header = "Special Certificate Admin"
admin.site.index_title = "Boshqaruv paneli"

urlpatterns = [
    path('admin/', admin.site.urls),

    # Bosh sahifa
    path('', include('apps.core.urls')),

    # Servislar
    path('services/', include('apps.services.urls')),

    # Galereya
    path('gallery/', include('apps.gallery.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)