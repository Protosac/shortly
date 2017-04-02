from django.test import TestCase
from django.urls import reverse

from .factories import UrlFactory, UserFactory
from .models import Url


class UrlModelTests(TestCase):
    def setUp(self):
        self.user = UserFactory(first_name='Barbara',
                                last_name='Tester',
                                email='barb@example.com')


    def test_create_new_url(self):
        new_url = Url.objects.create(label='Test Url',
                                     url='http://example.com',
                                     user=self.user)

        result = Url.objects.get(label='Test Url')
        self.assertEqual(result.uid, new_url.uid)


class UrlViewTests(TestCase):
    def setUp(self):
        self.user = UserFactory(first_name='Tony',
                                last_name='Tester',
                                email='tony@example.com')
        self.url = Url.objects.create(label='Test Url',
                                     url='http://example.com',
                                     user=self.user)

    def test_redirect_to_website(self):
        goto = reverse('url', kwargs={'uid': self.url.uid})
        response = self.client.get(goto)

        msg = "{0} does not equal {1}".format(response.url, 'http://example.com')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, 'http://example.com', msg=msg)
