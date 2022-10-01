from django.db import models
from django.contrib.auth.models import AbstractUser


class BookUser(AbstractUser):
    avatar = models.ImageField(
        upload_to="users_avatars", default="users_avatars/default.png", blank=True
    )
    age = models.PositiveIntegerField(default=18)
    country = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=128, blank=True)
    street = models.CharField(max_length=128, blank=True)
    street_number = models.PositiveIntegerField(null=True)
    postcode = models.PositiveIntegerField(null=True)
