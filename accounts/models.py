from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from shortuuidfield import ShortUUIDField

# from core.models import Url
from core.utils import create_uuid


class Profile(models.Model):
    uuid = ShortUUIDField(default=create_uuid, unique=True, help_text='User public id.')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
