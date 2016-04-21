from rest_framework import serializers
from django.contrib.auth.models import Group
from django.core.exceptions import *
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

class BusinessUserSerializer(serializers.ModelSerializer):
    class Meta:
        model =BusinessUser


class UserModelSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    student = StudentSerializer(read_only=True,many=True)
    business_user = BusinessUserSerializer(read_only=True)
    Business = BusinessSerializer(read_only=True,many=True,source='business_staff')
    University = UniversitySerializer(read_only=True,many=True,source='universityStaff')
    class Meta:
        model = User
        fields = ('id', 'first_name','last_name','username','email','password','student','business_user','Business','University')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        newUser=User.objects.create(**validated_data)
        newUser.set_password(validated_data['password'])
        newUser.save()
        return newUser
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance
