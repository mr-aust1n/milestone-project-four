from django.urls import path

from . import views

urlpatterns = [
    path("buy/<int:item_id>/", views.create_checkout_session, name="buy_item"),
    path("success/<int:item_id>/", views.payment_success, name="payment_success"),
    path("offer/<int:item_id>/", views.make_offer, name="make_offer"),
    path("accept/<int:offer_id>/", views.accept_offer, name="accept_offer"),
    path("reject/<int:offer_id>/", views.reject_offer, name="reject_offer"),
    path("orders/", views.my_orders, name="my_orders"),
    path("my-offers/", views.my_offers, name="my_offers"),
]
