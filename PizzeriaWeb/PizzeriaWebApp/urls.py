from django.contrib import admin
from django.urls import path
from PizzeriaWebApp import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.login, name="login"),
    path("login/", views.login, name="login"),
    path("registro/", views.registro, name="registro"),
    path("menu/", views.menu, name="menu"),
    path("pizza/", views.pizza, name="pizza"),
    path('datos/', views.datos, name='datos'),
    path("datos_usuarios/", views.datos_usuarios, name="datos_usuarios"),
    path("pedidos/", views.pedidos, name="pedidos"),
]
