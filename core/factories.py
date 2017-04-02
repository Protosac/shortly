import factory
import factory.django
import factory.fuzzy

from .models import Url
from accounts.models import User
from core.utils import short_url


class UrlFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Url

    uid = factory.fuzzy.FuzzyText(length=8)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
