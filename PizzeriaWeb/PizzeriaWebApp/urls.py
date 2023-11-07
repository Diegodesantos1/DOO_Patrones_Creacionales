from django.contrib import admin
from django.urls import path
from PizzeriaWebApp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.menu, name="menu"),
    path("pizza/", views.pizza, name="pizza"),
    path("registro/", views.registro, name="registro"),
]
