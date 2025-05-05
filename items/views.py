# items/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ItemForm
from .models import Item


def home(request):
    items = Item.objects.filter(is_sold=False).order_by("-date_posted")
    return render(request, "items/home.html", {"items": items})


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
    return render(request, "items/item_detail.html", {"item": item})


from django.contrib import messages


@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id, seller=request.user)

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
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
