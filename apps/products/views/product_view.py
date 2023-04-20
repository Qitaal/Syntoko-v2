from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import generics, viewsets, status, filters
from rest_framework.response import Response

from helpers.pagination import ResponsePagination
from ..models import Product
from ..serializers.product_serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    pagination_class = ResponsePagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name', 'sku']
    ordering_fields = '__all__'
    ordering = ['-updated_at']
