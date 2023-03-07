from django.contrib import admin
from django.urls import path
from servicios import views


urlpatterns = [
    path('', views.services),
]