from django.db import models
from authapp.models import BookUser
from mainapp.models import Book


class CartManager(models.Manager):
    def total_quantity(self):
        return sum(item.quantity for item in self.all())

    def total_price(self):
        return sum(item.book.price * item.quantity for item in self.all())


class Cart(models.Model):
    user = models.ForeignKey(BookUser, on_delete=models.CASCADE, related_name="cart")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def cost(self):
        return self.quantity * self.book.price
