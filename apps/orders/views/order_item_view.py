from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.orders.models import OrderItem
from apps.orders.serializers.order_item_serializer import OrderItemSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.filter(is_active=True)
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        order_pk = self.kwargs.get('order_pk')
        if order_pk:
            return self.queryset.filter(order__pk=order_pk)
        return self.queryset

    @action(detail=False, methods=['put'])
    def create_update_delete_item(self, request, order_pk=None):
        serializer = OrderItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        product = data.get('product')

        subtotal = product.selling_price * data.get('quantity')

        with transaction.atomic():
            order_item, created = OrderItem.objects.get_or_create(
                order_id=order_pk,
                product=product,
                is_active=True,
                defaults={
                    'quantity': data.get('quantity'),
                    'subtotal': subtotal,
                    'unit_price': product.selling_price
                }
            )
            order = order_item.order

            if data.get('quantity') == 0:
                order.total_amount -= order_item.subtotal
                order.save()
                order_item.delete()

                return Response(status=status.HTTP_204_NO_CONTENT)

            if created:
                order.total_amount += subtotal
                order.save()
            else:
                old_subtotal = order_item.subtotal
                order.total_amount -= old_subtotal
                order.total_amount += subtotal
                order.save()

                order_item.quantity = data.get('quantity')
                order_item.subtotal = subtotal
                order_item.unit_price = product.selling_price
                order_item.save()

            response_serializer = OrderItemSerializer(order_item)

            return Response(response_serializer.data, status=status.HTTP_200_OK)
