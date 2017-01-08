from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class Url(models.Model):
    label = models.CharField(max_length=255, help_text='Custom label for url.')
    uuid = models.UUIDField(unique=True, help_text='Short url identifier.')
    url = models.URLField(help_text='Destination url.')
    custom_id = models.CharField(unique=True, help_text='Custom short url identifier.')
    user = models.ForeignKey('User', on_delete=models.CASCADE)


class Owner(AbstractUser):
    email = models.EmailField()
    uuid = models.UUIDField(unique=True, help_text='User public id.')
    password = models.CharField(max_length=255)
    urls = models.ForeignKey(on_delete=models.CASCADE, help_text='Urls created by this user.')

