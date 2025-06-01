# orders/views.py

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from checkout.models import Order  # assuming Order model lives in checkout app


@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, buyer=request.user)

    if request.method == "POST":
        order.delete()
        messages.success(request, "Order deleted successfully.")
        return redirect("my_orders")

    return redirect("my_orders")


@login_required
def delete_offer(request, offer_id):
    offer = get_object_or_404(Order, id=offer_id, buyer=request.user, is_offer=True)

    if request.method == "POST":
        offer.delete()
        messages.success(request, "Offer deleted successfully.")
        return redirect("my_offers")

    return redirect("my_offers")
