from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
    #usable_password = models.CharField(max_length=255, null=True, blank=True)