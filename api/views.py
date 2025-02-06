from django.db.models import Max
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Product
from api.serializers import ProductSerializer, ProductInfoSerializer

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_info(request):
    products = Product.object.all()
    serializer = ProductInfoSerializer(
        {
            'products':products,
            'count': len(products),
            'max_price': products.aggreate(max_price=Max('price'))['max_price']
        }
    )

