from django.db import models
from authapp.models import BookUser
from mainapp.models import Book


class Order(models.Model):
    FORMING = "FRM"
    SENT = "SNT"
    READY = "RDY"
    CANCELED = "CNL"

    STATUS = (
        (FORMING, "Forming"),
        (SENT, "Sent"),
        (READY, "Ready to be taken"),
        (CANCELED, "Canceled"),
    )
    user = models.ForeignKey(BookUser, on_delete=models.CASCADE, related_name="order")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=STATUS, default=FORMING)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"Current order: {self.id} "

    def summary(self):
        items = self.items.select_related()
        return {
            "total_cost": sum(map(lambda item: item.quantity * item.book.price, items)),
            "total_quantity": sum(map(lambda item: item.quantity, items)),
        }

    def delete(self, **kwargs):
        self.is_active = False
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def cost(self):
        return self.book.price * self.quantity
