from django.urls import path

from product.views import CategoryListAPIView, ProductListAPIView, OrderCreateAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('create-order/', OrderCreateAPIView.as_view(), name='order-create'),

]
