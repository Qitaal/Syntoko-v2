from rest_framework import serializers

from ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id', 'is_active', 'created_at', 'updated_at')
        extra_kwargs = {
            'description': {'required': False}
        }

    def create(self, validated_data):
        validated_data['is_active'] = True
        return super().create(validated_data)
