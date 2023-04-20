from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.order_item_view import OrderItemViewSet
from .views.order_view import OrderViewSet

app_name = 'apps.orders'

# order_router = DefaultRouter()
# order_router.register(r'', OrderViewSet, basename='order')
#
# urlpatterns = [
#     path('', include(order_router.urls))
#     # path('', OrderListView.as_view(), name='order-list'),
#     # path('create', OrderCreateView.as_view(), name='order-create'),
#     # path('<int:pk>', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail')
# ]

order_list = OrderViewSet.as_view({'get': 'list', 'post': 'create'})
order_detail = OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

order_item_list = OrderItemViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'create_update_delete_item'})
order_item_detail = OrderItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

urlpatterns = [
    path('', order_list, name='order-list'),
    path('<int:pk>/', order_detail, name='order-detail'),
    path('<int:order_pk>/items/', order_item_list, name='order-item-list'),
    path('<int:order_pk>/items/<int:pk>/', order_item_detail, name='order-item-detail'),
]