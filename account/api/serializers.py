from rest_framework import serializers
from datetime import datetime
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth import  get_user_model
from rest_framework.authtoken.models import Token



User = get_user_model()

class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'image',
            'username',
            'email',
            'bio',
            'gender',
            'token',
        ]

    def get_token(self , obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'image',
            'username',
            'email',
            'bio',
            'gender'
        ]



class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'} , write_only= True)
    password2 = serializers.CharField(style={'input_type':'password'} , write_only= True)
    
    class Meta:
        model = User
        fields = ['email','first_name','last_name','username','password','password2','gender','bio','image']

    def create(self, validate_data):
        user = super().create(validate_data)
        password = validate_data.get('password')
        # new_password = make_password(password)
        # user.password = new_password
        user.set_password(password)
        user.save()
        return user

    def validate(self, data):
        password = data.get('password')
        password2 = data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match'})
        return data


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)