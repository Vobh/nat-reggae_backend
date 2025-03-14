from rest_framework import serializers

from .models import Product

from useraccount.serializers import UserDetailSerializer

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