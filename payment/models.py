from django.db import models

from account.models import CustomUser


# Create your models here.


class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='transactions')
    amount = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    ref_id = models.TextField(blank=True, null=True)
    authority = models.TextField()
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'transaction'


