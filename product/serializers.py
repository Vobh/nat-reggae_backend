from rest_framework import serializers

from .models import Product, Reservation

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

class ReservationsListSerializer(serializers.ModelSerializer):
    roduct = ProductsListSerializer(read_only=True, many=False)
    class Meta:
        model = Reservation
        fields = (
            'id', 'start_date', 'end_date', 'number_of_nights', 'total_price', 'product'
        )