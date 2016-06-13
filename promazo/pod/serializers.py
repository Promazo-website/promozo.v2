from rest_framework import serializers
from django.contrib.auth.models import Group
from django.core.exceptions import *
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User

class podRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=podRole

class podSerializer(serializers.ModelSerializer):
    class Meta:
        model=pod

class podPermissions(serializers.ModelSerializer):
    class Meta:
        model=podPermissions

class podMembersSerializer(serializers.ModelSerializer):
    user= userSerializer()
    role= podRoleSerializer
    class Meta:
        model=podMembers