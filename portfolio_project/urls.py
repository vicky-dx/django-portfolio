from django.contrib import admin
from django.urls import path, include

# Imports add karein
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio_app.urls')),
]

# Yeh hissa add karein
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)