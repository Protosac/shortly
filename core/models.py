from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from core.utils import short_url

from shortuuidfield import ShortUUIDField


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Url(models.Model):
    label = models.CharField(max_length=255, help_text='Custom label for url.')
    uid = ShortUUIDField(
        default=short_url,
        unique=True,
        editable=False,
        help_text='Short url identifier.')
    url = models.URLField(help_text='Destination url.')
    custom_id = models.CharField(max_length=255, unique=True, help_text='Custom short url identifier.')
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
