from rest_framework import serializers
from django.contrib.auth.models import Group
from django.core.exceptions import *
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *

class ProjectRoleTypeSerializer(serializers.Serializer):
    class Meta:
        model = ProjectRoleType

class ProjectSerializer(serializers.Serializer):
    class Meta:
        model = Project

class ProjectTaskSerializer(serializers.Serializer):
    class Meta:
        model = ProjectTask

class ProjectRoleSerializer(serializers.Serializer):
    class Meta:
        model = ProjectRole

class ProjectPlaceSerializer(serializers.Serializer):
    class Meta:
        model = ProjectPlace