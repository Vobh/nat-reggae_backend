from django.urls import path

from . import api

urlpatterns = [
    path('', api.products_list, name='api_products_list'),
    path('sale/', api.sale_product, name='api_sale_product'),
]