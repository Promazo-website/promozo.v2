from django.shortcuts import render
from .models import *
from rest_framework.decorators import detail_route, list_route
from rest_framework import serializers
from .serializers import *
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from pod.models import *

class ProjectRoleTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectRoleTypeSerializer
    queryset = ProjectRoleType.objects.all()


class ProjectsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    @list_route()
    def all(self,request):
        queryset = Project.objects.filter(pod__in=[x.pod for x in podMembers.objects.filter(member=request.user)])
        ser = ProjectSerializer(queryset,many=True)
        return Response(ser.data)
    @detail_route(methods=['GET'])
    def available_users(self, request):
        queryset = User.objects.filter(is_active=True).exclude(id__in=[x.user.id for x in ProjectPlace.objects.filter(ProjectRole__project=self.get_object())])
        ser = userSerializer(queryset, manu=True)
        return Response(ser.data)

class ProjectTaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectTaskSerializer
    queryset = ProjectTask.objects.all()
    @detail_route()
    def project(self,request, pk):
        queryset = ProjectTask.objects.filter(project__id=pk)
        ser = ProjectTaskSerializer(queryset,many=True)
        return Response(ser.data)


class ProjectRoleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectRoleSerializer
    queryset = ProjectRole.objects.all()
    @detail_route()
    def project(self, request, pk):
        queryset = ProjectRole.objects.filter(project__id=pk)
        ser = ProjectRoleSerializer(queryset,many=True)
        return Response(ser.data)
    @list_route()
    def available(self,request):
        ser=AvailableRolesSerializer(ProjectRole.objects.filter(project__status="active"),many=True)
        return Response(ser.data)


class ProjectPlaceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectPlaceSerializer
    queryset = ProjectPlace.objects.all()
    @detail_route()
    def role(self, request, pk):
        queryset = ProjectPlace.objects.filter(ProjectRole__id=pk)
        ser = ProjectPlaceSerializer(queryset, many=True)
        return Response(ser.data)
    @detail_route()
    def project(self,request, pk):
        queryset = ProjectPlace.objects.filter(ProjectRole__project__id=pk)
        ser = ProjectPlaceSerializer(queryset, many=True)
        return Response(ser.data)