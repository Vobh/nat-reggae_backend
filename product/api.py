from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Product
from .serializers import ProductsListSerializer
from .forms import ProductForm

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def products_list(request):
    products = Product.objects.all()
    serializer = ProductsListSerializer(products, many=True)

    return JsonResponse ({
        'data': serializer.data
    })

@api_view(['POST', 'FILES'])
def create_product(request):
    form = ProductForm(request.POST, request.FILES)

    if form.is_valid():
        product = form.save(commit=False)
        product.vendor = request.user
        product.save()

        return JsonResponse({'success': True})
    else:
        print('error', form.errors, form.non_field_errors)
        return JsonResponse({'errors': form.errors.as_json()}, status=400)