from django.shortcuts import render
from .models import Product
from .serializers import ProductSerailizer
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
