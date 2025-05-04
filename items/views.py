# items/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ItemForm
from .models import Item


def home(request):
    items = Item.objects.filter(is_sold=False).order_by(
        "-date_posted"
    )  # optional: show only available items
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
