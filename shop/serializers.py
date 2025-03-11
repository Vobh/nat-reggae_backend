from rest_framework import serializers

from .models import Product, Sale

from useraccount.serializers import UserDetailSerializer

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

class SalesListSerializer(serializers.ModelSerializer):
    product = ProductsListSerializer(read_only=True, many=False)
    class Meta:
        model = Sale
        fields = (
            'id',
            'name', 
            'city',
            'street',
            'number',
            'cep',
            'state',     
            'product',
        )