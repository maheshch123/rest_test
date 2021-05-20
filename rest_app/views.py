from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Product, Category,Stock
from .serializers import ProductSerializers,CategorySerializers,StockSerializers
from rest_framework.filters import SearchFilter

# Create your views here.


class ProductsApi(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_class = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('product_name',)

class CategoryApi(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_class = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('title',)

class StockApi(viewsets.ModelViewSet):
    serializer_class = StockSerializers
    queryset = Stock.objects.all()
    permission_class = (IsAuthenticated,)

    