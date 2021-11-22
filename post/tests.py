from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from .models import Post

class SnackModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test_user',password='pass')

        self.post = Post.objects.create(
            seller = self.user,
            car_name = 'Tesla',
            car_model = 'X',
            description = 'Electric car'
        )

    
    def test_post_content(self):
        post = Post.objects.get(id=1)

        self.assertEqual(str(post.seller), 'test_user')
        self.assertEqual(post.car_name, 'Tesla')
        self.assertEqual(post.car_model, 'X')
        self.assertEqual(post.description, 'Electric car')

class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

