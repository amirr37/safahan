from django.urls import path

from product.views import CategoryListAPIView, ProductListAPIView, UserOrderCreateAPIView, UserOrderListAPIView, \
    CategoryProductListAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('create-order/', UserOrderCreateAPIView.as_view(), name='order-create'),
    path('user-orders/', UserOrderListAPIView.as_view(), name='user-order-list'),
    path('category/<int:category_id>/', CategoryProductListAPIView.as_view(), name='category-product-list'),
]
