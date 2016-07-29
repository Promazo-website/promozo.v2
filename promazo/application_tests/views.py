from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.

class QuestionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class QuestionDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class ApplicationTestList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationTestSerializer
    queryset = ApplicationTests.objects.all()


class ApplicationTestDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationTestSerializer
    queryset = ApplicationTests.objects.all()