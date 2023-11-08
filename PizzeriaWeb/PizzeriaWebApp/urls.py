from django.contrib import admin
from django.urls import path
from PizzeriaWebApp import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.login, name="login"),
    path("menu/", views.menu, name="menu"),
    path("pizza/", views.pizza, name="pizza"),
    path("registro/", views.registro, name="registro"),
    path('datos/', views.datos, name='datos'),
]
