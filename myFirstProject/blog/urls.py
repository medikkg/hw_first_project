from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    re_path('about', views.about, name="about_US"),
    re_path('articles', views.articles, name='articles'),
    re_path('currencies', views.currencies, name='currencies'),
]