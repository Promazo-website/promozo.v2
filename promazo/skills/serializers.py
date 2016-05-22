from rest_framework import serializers
from django.contrib.auth.models import Group
from django.core.exceptions import *
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *

class skillsSerializer(serializers.ModelSerializer):
    class Meta:
        model =skills

class skillQuestionAnswerActionSerializer(serializers.ModelSerializer):
    class Meta:
        model =skillQuestionAnswerAction

class skillScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model =  skillScores

class skillQuestionAnswersSerializer(serializers.ModelSerializer):
    actions = skillQuestionAnswerActionSerializer(serializers.ModelSerializer, many=True)
    class Meta:
        model = skillQuestionAnswers


class skillQuestionsSerializer(serializers.ModelSerializer):
    answers = skillQuestionAnswersSerializer(many=True,read_only=True)
    class Meta:
        model = skillQuestion

class userSkillAnswersSerializer(serializers.ModelSerializer):
    allAnswers = skillQuestionAnswersSerializer(read_only=True, many=True)
    question = skillQuestionsSerializer(read_only=True)
    class Meta:
        model = userSkillAnswers

class UserSkillsSerializer(serializers.Serializer):
    skill = skillsSerializer(read_only=True)
    validated = serializers.BooleanField()
    assigned = serializers.BooleanField()
