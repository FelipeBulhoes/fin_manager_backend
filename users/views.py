from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.generics import (
    CreateAPIView, ListAPIView
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']

class UserListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']