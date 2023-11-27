from django.contrib import admin
from product.models import Category, Product, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'weight')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    list_editable = ('price', 'stock', 'weight', 'category')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'order_date', 'total_amount', 'is_paid', 'is_delivered')
    list_filter = ('user', 'is_delivered')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'id')
    readonly_fields = ('total_amount',)
