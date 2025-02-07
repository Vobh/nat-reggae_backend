from rest_framework import serializers

from .models import Product

from useraccount.serializers import UserDetailSerializer

class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'price_per_night',
            'image_url',
        )

class ProductsDetailSerializer(serializers.ModelSerializer):
    vendor = UserDetailSerializer(read_only=True, many=False)
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'description',
            'price_per_night',
            'image_url',
            'days',
            'vendor'
        )