# items/Views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ItemForm


@login_required
def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return redirect("home")  # You’ll define this URL name
    else:
        form = ItemForm()
    return render(request, "items/add_item.html", {"form": form})
