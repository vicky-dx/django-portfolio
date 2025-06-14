from django.contrib import admin
from django.urls import path, include

# This is the main URL configuration for the entire project.
urlpatterns = [
    # The path for the Django admin site.
    path('admin/', admin.site.urls),
    
    # This line tells Django that for any URL that isn't 'admin/',
    # it should look for further instructions in the 'portfolio_app.urls' file.
    path('', include('portfolio_app.urls')),
]
