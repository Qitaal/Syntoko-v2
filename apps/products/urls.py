from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.category_view import CategoryViewSet
from .views.product_view import ProductViewSet

app_name = 'apps.products'

product_list = ProductViewSet.as_view({'get': 'list', 'post': 'create'})
product_detail = ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

category_list = CategoryViewSet.as_view({'get': 'list', 'post': 'create'})
category_detail = CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

urlpatterns = [
    path('', product_list, name='order-list'),
    path('<int:pk>/', product_detail, name='order-detail'),
    path('categories/', category_list, name='order-item-list'),
    path('categories/<int:pk>/', category_detail, name='order-item-detail'),
]