from django.db import models

from ...users.models import Customer, Employee


class Order(models.Model):
    PROCESSING = 'PROCESSING'
    PAID = 'PAID'
    SHIPPED = 'SHIPPED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'
    DRAFT = 'DRAFT'
    ORDER_STATUS_CHOICES = (
        (PROCESSING, 'PROCESSING'),
        (PAID, 'PAID'),
        (SHIPPED, 'SHIPPED'),
        (COMPLETED, 'COMPLETED'),
        (CANCELLED, 'CANCELLED'),
        (DRAFT, 'DRAFT')
    )

    order_number = models.CharField(max_length=255, unique=True)
    cashier = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=255, choices=ORDER_STATUS_CHOICES)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return self.order_number

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()
