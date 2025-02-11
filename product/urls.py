from django.urls import path
from . import api

urlpatterns = [
    path('', api.products_list, name='api_products_list'),
    path('create/', api.create_product, name='api_create_product'),
    path('<uuid:pk>/', api.products_detail, name='api_products_detail'),
    path('<uuid:pk>/book/', api.book_product, name='api_book_product'),
    path('<uuid:pk>/reservations/', api.product_reservations, name='api_product_reservations'),
    path('<uuid:pk>/toggle_favorite/', api.toggle_favorite, name='api_toggle_favorite'),
]