from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import ProductForm
from .models import Product, Reservation
from .serializers import ProductsListSerializer, ProductsDetailSerializer, ReservationsListSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def products_list(request):
    products = Product.objects.all()
    serializer = ProductsListSerializer(products, many=True)

    return JsonResponse ({
        'data': serializer.data
    })

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def products_detail(request, pk):
    product = Product.objects.get(pk=pk)

    serializer = ProductsDetailSerializer(product, many=False)

    return JsonResponse(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def product_reservations(request, pk):
    product = Product.objects.get(pk=pk)
    reservations = product.reservations.all()

    serializer = ReservationsListSerializer(reservations, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['POST', 'FILES']) # 8:23:06
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

@api_view(['POST'])
def book_product(request, pk):
    try:
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        number_of_nights = request.POST.get('number_of_nights', '')
        total_price = request.POST.get('total_price', '')
        days = request.POST.get('days', '')

        product = Product.objects.get(pk=pk)

        Reservation.objects.create(
            product=product,
            start_date=start_date,
            end_date=end_date,
            number_of_nights=number_of_nights,
            total_price=total_price,
            days=days,
            created_by=request.user
        )
        
        return JsonResponse({'success': True})
    except Exception as e:
        print('Error', e)

        return JsonResponse({'success': False})