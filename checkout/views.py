# checkout/views.py

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from items.models import Item

from .forms import OfferForm
from .models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def create_checkout_session(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

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
    item.is_sold = True
    item.save()

    Order.objects.create(
        item=item,
        buyer=request.user,
        price=item.price,
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
