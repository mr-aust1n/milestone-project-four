# checkout/views.py

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from items.models import Item

from .forms import OfferForm
from .models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def create_checkout_session(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    # Prevent checkout if out of stock
    if item.quantity < 1:
        messages.error(request, "Sorry, this item is out of stock.")
        return redirect("item_detail", item_id=item.id)

    if item.is_sold:
        return redirect("item_detail", item_id=item.id)

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "gbp",
                    "unit_amount": int(item.price * 100),
                    "product_data": {
                        "name": item.title,
                        "description": item.description,
                    },
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=request.build_absolute_uri(f"/checkout/success/{item.id}/"),
        cancel_url=request.build_absolute_uri(f"/{item.id}/"),
        customer_email=request.user.email,
    )

    return redirect(checkout_session.url, code=303)


@login_required
def payment_success(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    # Reduces quantity by 1
    item.quantity -= 1
    if item.quantity <= 0:
        item.is_sold = True
        item.quantity = 0  # Safety
    item.save()

    # Create the order record
    order = Order.objects.create(
        item=item,
        buyer=request.user,
        price=item.price,
    )

    # Send confirmation email
    send_mail(
        subject="ReLuvd - Order Confirmation",
        message=f"Hi {request.user.username},\n\nThank you for your order of '{item.title}'. Your payment has been received.\n\nRegards,\nThe ReLuvd Team",
        from_email=None,  # Uses DEFAULT_FROM_EMAIL from settings.py
        recipient_list=[request.user.email],
        fail_silently=False,
    )

    return render(request, "checkout/success.html", {"item": item})


@login_required
def make_offer(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if item.is_sold or item.seller == request.user:
        return redirect("item_detail", item_id=item.id)

    if request.method == "POST":
        form = OfferForm(request.POST)
        if form.is_valid():
            offer_price = form.cleaned_data["offer_price"]
            note = form.cleaned_data["note"]

            Order.objects.create(
                item=item,
                buyer=request.user,
                price=offer_price,
                is_offer=True,
                offer_note=note,
            )

            return render(request, "checkout/offer_submitted.html", {"item": item})
    else:
        form = OfferForm()

    return render(request, "checkout/make_offer.html", {"form": form, "item": item})


@login_required
def accept_offer(request, offer_id):
    offer = get_object_or_404(Order, id=offer_id, is_offer=True)

    if offer.item.seller != request.user:
        return redirect("dashboard")

    offer.status = "accepted"
    offer.save()
    messages.success(request, "Offer accepted.")
    return redirect("dashboard")


@login_required
def reject_offer(request, offer_id):
    offer = get_object_or_404(Order, id=offer_id, is_offer=True)

    if offer.item.seller != request.user:
        return redirect("dashboard")

    offer.status = "rejected"
    offer.save()
    messages.info(request, "Offer rejected.")
    return redirect("dashboard")


@login_required
def my_orders(request):
    orders = (
        Order.objects.filter(buyer=request.user)
        .select_related("item")
        .order_by("-created_at")
    )
    return render(request, "checkout/my_orders.html", {"orders": orders})


@login_required
def my_offers(request):
    offers = Order.objects.filter(buyer=request.user, is_offer=True).select_related(
        "item"
    )
    return render(request, "checkout/my_offers.html", {"offers": offers})
