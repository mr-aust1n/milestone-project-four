from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from checkout.models import Order

from .forms import ItemForm, MessageForm
from .models import Item, Message


def home(request):
    category = request.GET.get("category")
    sort = request.GET.get("sort")

    items = Item.objects.all()

    if category:
        items = items.filter(category=category)

    if sort == "price_asc":
        items = items.order_by("price")
    elif sort == "price_desc":
        items = items.order_by("-price")
    elif sort == "title_asc":
        items = items.order_by("title")
    elif sort == "title_desc":
        items = items.order_by("-title")

    # Build your categories list as you're already doing:
    categories = Item.CATEGORY_CHOICES  # or however you're generating it

    context = {
        "items": items,
        "categories": categories,
        "selected_category": category,
        "selected_sort": sort,
    }
    return render(
        request,
        "items/home.html",
        {"items": items, "categories": categories, "selected_category": category},
    )


@login_required
def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return redirect("home")
    else:
        form = ItemForm()
    return render(request, "items/add_item.html", {"form": form})


def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    messages = item.messages.select_related("sender")

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.item = item
            message.sender = request.user
            message.save()

            # ✅ Email alert to seller
            send_mail(
                subject=f"New message about your item: {item.title}",
                message=(
                    f"You've received a new message from {request.user.username}:\n\n"
                    f"{message.message}\n\n"
                    f"View the item here: http://127.0.0.1:8000/{item.id}/"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[item.seller.email],
                fail_silently=True,
            )

            return redirect("item_detail", item_id=item.id)
    else:
        form = MessageForm()

    return render(
        request,
        "items/item_detail.html",
        {"item": item, "form": form, "messages": messages},
    )


@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id, seller=request.user)

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            # Check if a new image was uploaded
            if not request.FILES.get("image"):
                form.instance.image = item.image  # retain existing image

            form.save()
            messages.success(request, "Item updated successfully.")
            return redirect("item_detail", item_id=item.id)
    else:
        form = ItemForm(instance=item)

    return render(request, "items/edit_item.html", {"form": form, "item": item})


@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id, seller=request.user)

    if request.method == "POST":
        item.delete()
        messages.success(request, "Item deleted successfully.")
        return redirect("home")

    return render(request, "items/delete_item.html", {"item": item})


@login_required
def dashboard(request):
    my_items = Item.objects.filter(seller=request.user)
    offers = Order.objects.filter(item__in=my_items, is_offer=True).select_related(
        "item", "buyer"
    )
    messages = Message.objects.filter(item__seller=request.user).select_related(
        "item", "sender"
    )

    return render(
        request,
        "items/dashboard.html",
        {"my_items": my_items, "offers": offers, "messages": messages},
    )
