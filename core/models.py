from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from core.utils import short_url

from shortuuidfield import ShortUUIDField


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Url(models.Model):
    label = models.CharField(max_length=255, help_text='Name for url.')
    uid = ShortUUIDField(
        default=short_url,
        unique=True,
        editable=False,
        help_text='Short url identifier.')
    url = models.URLField(help_text='Destination url.')
    custom_id = models.CharField(max_length=255,
                                 unique=True,
                                 default=uid,
                                 help_text='Custom name for destination.',
                                 null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))

    def __str__(self):
        return "Url to: {0}".format(self.url)

    @property
    def link(self):
        return reverse('url', kwargs={'uid': self.uid})

    @property
    def u_custom_id(self):
        if not self.custom_id:
            return self.uid
