from django.forms import ModelForm

from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = (
            'title',
            'description',
            'price_per_night',
            'days',
            'country',
            'country_code',
            'category',
            'image',
        )