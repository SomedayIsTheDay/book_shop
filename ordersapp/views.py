from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Order, OrderItem


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "ordersapp/order.html"

    def get_object(self, queryset=None):
        order = Order.objects.filter(pk=self.kwargs.get("pk")).select_related().first()
        if not order:
            return HttpResponseBadRequest()
        return order


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "ordersapp/order_list.html"

    def get_queryset(self):
        return (
            Order.objects.filter(user=self.request.user, is_active=True)
            .select_related()
            .order_by("created_at")
        )


@transaction.atomic
@login_required
def create(request):
    cart = getattr(request.user, "cart").all()
    if not cart:
        return HttpResponseRedirect(reverse("books:index"))
    order = Order(user=request.user)
    order.save()
    for item in cart:
        item = OrderItem(order=order, book=item.book, quantity=item.quantity)
        item.save()
    cart.delete()
    return HttpResponseRedirect(reverse("orders:orders"))


@login_required
def cancel(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if not order.status == "FRM":
        return HttpResponseBadRequest()

    order.status = Order.CANCELED
    order.delete()
    return HttpResponseRedirect(reverse("orders:orders"))
