from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Cart
from mainapp.models import Book


@login_required
def cart(request):
    cart_obj = Cart.objects.filter(user=request.user).select_related().all()
    return render(
        request,
        "cartapp/cart.html",
        context={"title": "Cart", "cart": cart_obj},
    )


@login_required
def add(request, pk):
    book = get_object_or_404(Book, pk=pk)
    cart_obj = Cart.objects.filter(user=request.user, book=book).first()

    if not cart_obj:
        cart_obj = Cart(user=request.user, book=book)

    cart_obj.quantity += 1
    cart_obj.save()

    if "login" in request.META.get("HTTP_REFERER"):
        return HttpResponseRedirect(reverse("mainapp:book", args=[pk]))

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"), reverse("index"))


@login_required
def remove(request, pk):
    cart_obj = get_object_or_404(Cart, pk=pk)
    cart_obj.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"), reverse("index"))


@login_required
def edit(request, pk, quantity):
    cart_item = get_object_or_404(Cart, pk=pk)
    cart_item.quantity = quantity
    if cart_item.quantity == 0:
        cart_item.delete()
    else:
        cart_item.save()
    cart_obj = Cart.objects.filter(user=request.user).select_related().all()
    return render(
        request, "cartapp/includes/cart_list.html", context={"cart": cart_obj}
    )
