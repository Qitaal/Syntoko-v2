import time

from django.db import transaction
from rest_framework import serializers

from Shared.helpers import generate_order_number
from apps.orders.models import OrderItem
from apps.orders.models.order import Order
from apps.orders.serializers.order_item_serializer import OrderItemSerializer
from apps.products.models import Product
from apps.users.models import Employee, Customer


class OrderSerializer(serializers.ModelSerializer):
    cashier_id = serializers.PrimaryKeyRelatedField(source='cashier', queryset=Employee.objects.filter(is_active=True))
    customer_id = serializers.PrimaryKeyRelatedField(source='customer',
                                                     queryset=Customer.objects.filter(is_active=True), required=False)
    order_items = OrderItemSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = ('id', 'cashier_id', 'customer_id', 'order_number', 'status', 'order_items', 'total_amount')
        read_only_fields = ('id', 'order_number', 'status', 'order_items', 'total_amount')

    def create(self, validated_data):
        order_number = generate_order_number()
        validated_data['order_number'] = order_number

        validated_data['status'] = Order.PROCESSING
        try:
            return Order.objects.create(**validated_data)
        except Exception as e:
            raise e

    def update(self, instance, validated_data):
        if 'customer' not in validated_data:
            instance.customer = None
        return super().update(instance, validated_data)
