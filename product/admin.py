from django.contrib import admin
from product.models import Category, Product, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'weight')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    list_editable = ('price', 'stock', 'weight', 'category')


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'total_amount', 'is_completed')
    list_filter = ('user', 'is_completed')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'id')
    inlines = [OrderItemInline]
    readonly_fields = ('total_amount',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'subtotal')
    list_filter = ('order__user', 'product')
    search_fields = (
        'order__user__username', 'order__user__first_name', 'order__user__last_name', 'product__name', 'id')
    readonly_fields = ('subtotal',)
