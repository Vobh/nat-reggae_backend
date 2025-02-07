from django.urls import path
from . import api

urlpatterns = [
    path('', api.products_list, name='api_products_list'),
    path('create/', api.create_product, name='api_create_product'),
]