from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('quick_user.api_urls')),
]