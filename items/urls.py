# items/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_item, name="add_item"),
    path("<int:item_id>/", views.item_detail, name="item_detail"),
]
