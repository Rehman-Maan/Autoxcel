from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("vehicles", views.vehicles, name="vehicles"),
    path("form", views.form, name="form"),
    path("payment", views.payment, name="payment")
]