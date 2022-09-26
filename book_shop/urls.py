from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", mainapp.index, name="index"),
    path("contacts/", mainapp.contacts, name="contacts"),
    path("books/", include("mainapp.urls", namespace="books")),
    path("auth/", include("authapp.urls", namespace="auth")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
