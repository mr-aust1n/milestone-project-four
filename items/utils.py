# items/utils.py
from django.db.models import Q

from checkout.models import Order

from .models import Item, Message


def get_notifications(user):
    if not user.is_authenticated:
        return []

    items = Item.objects.filter(seller=user)

    # New messages
    message_notes = Message.objects.filter(item__in=items).order_by("-created_at")[:5]

    # New offers
    offer_notes = Order.objects.filter(item__in=items, is_offer=True).order_by(
        "-created_at"
    )[:5]

    # Items sold
    sold_notes = Item.objects.filter(seller=user, is_sold=True).order_by(
        "-date_posted"
    )[:5]

    return {
        "messages": message_notes,
        "offers": offer_notes,
        "sales": sold_notes,
    }
