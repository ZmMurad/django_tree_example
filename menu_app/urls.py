from django.urls import path, include
from menu_app.views import home_view, catalog_view, user_view

urlpatterns = [
    path('', home_view, name='home'),
    path('catalogs', catalog_view, name='catalog'),
    path('users', user_view, name='users'),
]
