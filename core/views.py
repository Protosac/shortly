from django.shortcuts import redirect

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .models import Url


class UrlView(APIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        """
        Accepts a UID and redirects user to Url.url
        :param args: Request object
        :return: redirect user to website
        """
        destination = Url.objects.get(uid=kwargs.get('uid'))
        return redirect(destination.url, permanent=True)

url_redirect = UrlView.as_view()
