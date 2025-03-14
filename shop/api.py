from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import SaleForm
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

@api_view(['POST'])
def create_sale(request):
    form = SaleForm(request.POST)
    if form.is_valid():
        sale = form.save(commit=False)
        sale.client = request.user
        sale.save()

        return JsonResponse({'success': True})
    else:
        print('error', form.errors, form.non_field_errors)
        return JsonResponse({'errors': form.errors.as_json()}, status=400)

    