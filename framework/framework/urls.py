from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('unixni.urls')),
    path('accounts/', include('allauth.urls')),  # Adds urls for login, logout, register, etc.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
