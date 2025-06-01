# accounts/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.register, name="signup"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
