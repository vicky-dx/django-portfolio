from django.urls import path
from . import views

# This is the URL configuration for the 'portfolio_app'.
# The name 'home' allows us to easily refer to this URL pattern from other parts of Django.
urlpatterns = [
    # When a user visits the root URL of our app (''), Django will call the portfolio_view function.
    path('', views.portfolio_view, name='home'),
]
