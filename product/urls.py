from django.urls import path

from product.views import CategoryListAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),

]
