from rest_framework import serializers

from ..models import Category
from ..models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(source='category', queryset=Category.objects.filter(is_active=True))

    class Meta:
        model = Product
        fields = ('id', 'name', 'sku', 'description', 'purchase_price', 'selling_price', 'image', 'stock', 'category_id', 'is_active', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at', 'is_active', 'id')
        extra_kwargs = {
            'description': {'required': False},
            'image': {'required': False},
            'is_active': {'required': False}
        }

    def create(self, validated_data):
        validated_data['is_active'] = True
        return super().create(validated_data)
