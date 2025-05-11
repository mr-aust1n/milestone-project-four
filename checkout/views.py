# checkout / views.py

import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from items.models import Item

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
