from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    User._meta.get_field('email')._unique = True
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=20, unique=True)
    rating = models.IntegerField()