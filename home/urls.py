"""Myweb URL Configuration
"""

from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('thankyou/', views.thankyou, name="thankyou")
]
