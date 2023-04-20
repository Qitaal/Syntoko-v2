from rest_framework import viewsets
from ..models import Order
from ..serializers.order_serializer import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter(is_active=True)
    serializer_class = OrderSerializer
