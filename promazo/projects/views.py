from django.shortcuts import render
from .models import *

from rest_framework import serializers
from .serializers import *

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ProjectRoleTypeList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectRoleTypeSerializer
    queryset = ProjectRoleType.objects.all()

class ProjectRoleTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectRoleTypeSerializer
    queryset = ProjectRoleType.objects.all()

class ProjectList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectTaskList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectTaskSerializer
    queryset = ProjectTask.objects.all()

class ProjectTaskDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectTaskSerializer
    queryset = ProjectTask.objects.all()

class ProjectRoleList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectRoleSerializer
    queryset = ProjectRole.objects.all()


class ProjectRoleDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectRoleSerializer
    queryset = ProjectRole.objects.all()


class ProjectPlaceList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectPlaceSerializer
    queryset = ProjectPlace.objects.all()

class ProjectPlaceDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectPlaceSerializer
    queryset = ProjectPlace.objects.all()