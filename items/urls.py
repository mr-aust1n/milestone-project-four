# items/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_item, name="add_item"),
    path("<int:item_id>/", views.item_detail, name="item_detail"),
    path("<int:item_id>/edit/", views.edit_item, name="edit_item"),
    path("<int:item_id>/delete/", views.delete_item, name="delete_item"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
