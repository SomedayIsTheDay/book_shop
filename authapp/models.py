from django.db import models
from django.contrib.auth.models import AbstractUser


class BookUser(AbstractUser):
    avatar = models.ImageField(
        upload_to="users_avatars", default="users_avatars/default.png", blank=True
    )
    age = models.PositiveIntegerField()
