from django.contrib import admin
from django.urls import path
from PizzeriaWebApp import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("menu/", views.menu, name="menu"),
    path("pizza/", views.pizza, name="pizza"),
]
