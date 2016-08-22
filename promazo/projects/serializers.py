from rest_framework import serializers
from django.contrib.auth.models import Group
from django.core.exceptions import *
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User


class ProjectRoleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRoleType

class AvailableRolesSerializer(serializers.ModelSerializer):
    freePlaces = serializers.IntegerField(read_only=True)
    class Meta:
        model = ProjectRole

class ProjectSerializer(serializers.ModelSerializer):
    no_tasks = serializers.IntegerField(read_only=True)
    no_roles = serializers.IntegerField(read_only=True)
    no_places = serializers.IntegerField(read_only=True)
    class Meta:
        model = Project

class ProjectTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTask

class ProjectRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRole

class ProjectPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPlace