from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from djoser.serializers import UserCreateSerializer , UserSerializer
from core_user.models import User
from django.contrib.auth.hashers import make_password


class MyCreateUser(ModelSerializer):
    
    def validate_password(self, value):
        return make_password(value)
    
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    class Meta(UserCreateSerializer.Meta):
        fields = [
            'first_name',
            'last_name',
            'email',
            'password'
        ]
        

class UserInfoSerializer(ModelSerializer):
    
    class Meta(UserSerializer.Meta):
        pass