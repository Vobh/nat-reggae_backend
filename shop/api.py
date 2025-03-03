from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Product
from .serializers import ProductsListSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def products_list(request):
    products = Product.objects.all()
    serializer = ProductsListSerializer(products, many=True)

    return JsonResponse({
        'data': serializer.data
    })