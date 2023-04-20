from django.db import models

from .order import Order
from ...products.models import Product


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders_item'
        indexes = [
            models.Index(fields=['order_id', 'product_id', 'is_active'])
        ]

    def __str__(self):
        return f'{self.product} x {self.quantity}'

    # def delete(self, using=None, keep_parents=False):
    #     self.is_active = False
    #     self.save()
