from django.urls import path

from . import views

urlpatterns = [
    path("buy/<int:item_id>/", views.create_checkout_session, name="buy_item"),
    path("success/<int:item_id>/", views.payment_success, name="payment_success"),
    path("offer/<int:item_id>/", views.make_offer, name="make_offer"),
]
