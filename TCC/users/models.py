from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    interests = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    # campos extras para gamificação (opcional agora)
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.username
