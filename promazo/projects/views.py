from django.shortcuts import render
from .models import *

from rest_framework import serializers
from .serializers import *
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ProjectRoleTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectRoleTypeSerializer
    queryset = ProjectRoleType.objects.all()


class ProjectsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectTaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectTaskSerializer
    queryset = ProjectTask.objects.all()


class ProjectRoleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectRoleSerializer
    queryset = ProjectRole.objects.all()


class ProjectPlaceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectPlaceSerializer
    queryset = ProjectPlace.objects.all()
