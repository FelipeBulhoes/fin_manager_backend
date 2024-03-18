from django.urls import path

from .views import UserCreateView, UserListView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("create/", UserCreateView.as_view(), name="create"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("list/", UserListView.as_view(), name="list"),
]