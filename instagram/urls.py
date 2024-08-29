from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from instagram import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("webapp.urls")),
    path('accounts/', include("accounts.urls")),
    path('api/', include('api_v1.urls')),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
