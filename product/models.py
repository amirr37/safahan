from django.db import models
from account.models import CustomUser
from django.core.validators import MinValueValidator


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField()
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=0, default=0, validators=[MinValueValidator(0)])
    is_completed = models.BooleanField(default=False)
    shipping_address = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True)

    # def calculate_total_amount(self):
    #     return sum(item.subtotal for item in self.order_items.all())

    def save(self, *args, **kwargs):
        # self.total_amount = self.calculate_total_amount() or 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.pk} - {self.user.get_full_name()}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=0, validators=[MinValueValidator(0)], blank=True)

    # def save(self, *args, **kwargs):
    # super().save(*args, **kwargs)
    # self.subtotal = self.product.price * self.quantity
    # super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.pk}"
