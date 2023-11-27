from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from product.models import Category, Product, Order
from product.serializers import CategorySerializer, ProductSerializer, OrderSerializer


# Create your views here.


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



class UserOrderListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter orders based on the current user
        return Order.objects.filter(user=self.request.user)