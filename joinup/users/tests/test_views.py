from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterViewTests(APITestCase):
    def test_create_user_success(self):
        url = reverse('users:signup', kwargs={'version_api': 'v1'})
        data = {
            'name': 'Test User',
            'last_name': 'Last Name',
            'email': 'test@example.com',
            'phone': '1234567890',
            'hobbies': 'Reading, Coding',
            'password': 'testpassword123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'test@example.com')

    def test_create_user_invalid_data(self):
        url = reverse('users:signup', kwargs={'version_api': 'v1'})
        data = {}  # Empty data
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserProfileViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', name='Test', last_name='User', phone='1234567890', hobbies='Reading, Coding', password='testpassword123')
        self.url = reverse('users:profile', kwargs={'version_api': 'v1'})

    def test_get_user_profile_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_profile_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@example.com')
