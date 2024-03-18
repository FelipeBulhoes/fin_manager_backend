from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from .models import User
from .serializers import UserSerializer
from .views import UserCreateView, UserListView

# Create your tests here.
class UserTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.userData = {
            'username': 'fulano',
            'email': 'fulano@gmail.com',
            'password': '123456'
        }

    def testUserCreation(self):
        request = self.factory.post('/users/create/', self.userData, format='json')
        view = UserCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def testUserList(self):
        user = User.objects.create_user(self.userData)
        view = UserListView.as_view()

        request = self.factory.get('/users/list/')
        force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)