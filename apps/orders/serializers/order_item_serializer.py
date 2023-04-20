from django.db import transaction
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from ..models.order_item import OrderItem
from ..models.order import Order
from ...products.models.product import Product


class ActiveOrderItemSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(is_active=True)
        return super(ActiveOrderItemSerializer, self).to_representation(data)


class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(source='product', queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ('id', 'order_id', 'product_id', 'quantity', 'unit_price', 'subtotal')
        read_only_fields = ('id', 'order_id', 'created_at', 'updated_at', 'unit_price', 'subtotal')
        list_serializer_class = ActiveOrderItemSerializer

    # def create(self, validated_data):
    #     order_id = self.context['view'].kwargs.get('order_pk')
    #     order = get_object_or_404(Order, id=order_id)
    #     validated_data['order'] = order
    #
    #     product = validated_data['product']
    #     validated_data['unit_price'] = product.selling_price
    #
    #     quantity = validated_data['quantity']
    #     subtotal = product.selling_price * quantity
    #     validated_data['subtotal'] = subtotal
    #
    #     try:
    #         with transaction.atomic():
    #             order_item = OrderItem.objects.create(**validated_data)
    #             order.total_amount += subtotal
    #             order.save()
    #
    #         return order_item
    #     except Exception as e:
    #         raise e
    #
    # def update(self, instance, validated_data):
    #     old_amount = instance.subtotal
    #
    #     order_id = self.context['view'].kwargs.get('order_pk')
    #     order = get_object_or_404(Order, id=order_id)
    #
    #     product = validated_data['product']
    #     instance.unit_price = product.selling_price
    #
    #     quantity = validated_data['quantity']
    #     instance.quantity = quantity
    #
    #     subtotal = product.selling_price * quantity
    #     instance.subtotal = subtotal
    #
    #     try:
    #         with transaction.atomic():
    #             instance.save()
    #
    #             order.total_amount -= old_amount
    #             order.total_amount += subtotal
    #             order.save()
    #
    #             return instance
    #     except Exception as e:
    #         raise e
