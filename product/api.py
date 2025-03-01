from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.tokens import AccessToken

from .forms import ProductForm
from .models import Product, Reservation
from .serializers import ProductsListSerializer, ProductsDetailSerializer, ReservationsListSerializer
from useraccount.models import User

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def products_list(request):
    #
    # Auth

    try:
        token = request.META['HTTP_AUTHORIZATION'].split('Bearer ')[1]
        token = AccessToken(token)
        user_id = token.payload['user_id']
        user = User.objects.get(pk=user_id)
    except Exception as e:
        user = None

    #
    #

    favorites = []
    products = Product.objects.all()

    #
    # Filter

    is_favorites = request.GET.get('is_favorites', '')
    vendor_id = request.GET.get('vendor_id', '')

    country = request.GET.get('country', '')
    category = request.GET.get('category', '')
    checkin_date = request.GET.get('checkIn', '')
    checkout_date = request.GET.get('checkOut', '')
    days = request.GET.get('numDays', '')

    if checkin_date and checkout_date:
        exact_matches = Reservation.objects.filter(start_date=checkin_date) | Reservation.objects.filter(end_date=checkout_date)
        overlap_matches = Reservation.objects.filter(start_date__lte=checkout_date, end_date__gte=checkin_date)
        all_matches = []

        for reservation in exact_matches | overlap_matches:
            all_matches.append(reservation.product_id)

            products = products.exclude(id__in=all_matches)

    if vendor_id:
        products = products.filter(vendor_id=vendor_id)
    
    if is_favorites:
        products = products.filter(favorited__in=[user])
    
    if days:
        products = products.filter(days__gte=days)

    if country:
        products = products.filter(country=country)

    if category and category != 'undefined':
        products = products.filter(category=category)
    
    #
    # Favorites

    if user:
        for product in products:
            if user in product.favorited.all():
                favorites.append(product.id)
    
    #
    # 
    serializer = ProductsListSerializer(products, many=True)

    return JsonResponse ({
        'data': serializer.data,
        'favorites': favorites
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

@api_view(['POST'])
def toggle_favorite(request, pk):
    product = Product.objects.get(pk=pk)

    if request.user in product.favorited.all():
        product.favorited.remove(request.user)

        return JsonResponse({'is_favorite': False})
    else:
        product.favorited.add(request.user)

        return JsonResponse({'is_favorite': True})