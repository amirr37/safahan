from django.db import models
from django.contrib.auth.models import AbstractUser


################################
# superuser information
# username : admin
# email : amirrj037@gmail.com
# password : admin
################################


# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return self.username
