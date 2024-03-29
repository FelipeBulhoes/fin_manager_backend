from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = '__all__'