from rest_framework import serializers

from .models import Product

class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'currency',
            'image_url',
            'imageAlt',
        )