# orders/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path("delete/<int:order_id>/", views.delete_order, name="delete_order"),
    path("delete-offer/<int:offer_id>/", views.delete_offer, name="delete_offer"),
]
