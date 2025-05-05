# accounts/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.register, name="signup"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
]
