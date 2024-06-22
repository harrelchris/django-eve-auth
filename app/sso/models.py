from django.db import models
from django.utils import timezone


class Token(models.Model):
    character_id = models.IntegerField()
    character_name = models.CharField(max_length=256)
    access_token = models.CharField(max_length=8192)
    expiration = models.DateTimeField()
    refresh_token = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.character_name} - {self.expiration}"
