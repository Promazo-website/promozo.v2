from rest_framework import serializers
from django.contrib.auth.models import Group
from django.core.exceptions import *
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *

class QuestionSerializer(serializers.Serializer):
    class Meta:
        model = Question

class ApplicationTestSerializer(serializers.Serializer):
    class Meta:
        model = ApplicationTests