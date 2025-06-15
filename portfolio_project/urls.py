from django.contrib import admin
from django.urls import path, include

# Imports add karein
from django.conf import settings
from django.conf.urls.static import static

from portfolio_app.views import create_admin_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio_app.urls')),
    path('create-admin/', create_admin_user, name='create_admin_user'),
]

# Yeh hissa add karein
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)