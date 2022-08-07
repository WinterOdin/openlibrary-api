from django.urls import path
from .views import render_main

urlpatterns = [
    path('', render_main, name='download_books'),
]
