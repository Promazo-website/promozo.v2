from rest_framework import serializers
from django.contrib.auth.models import Group
from django.core.exceptions import *
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application

class ApplicationNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationNotes

class AssignedTestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedTest

class ApplicantTestResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantTestResults

class ApplicationCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationCases

class ApplicationCaseResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ApplicationCaseResults