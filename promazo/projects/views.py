from django.shortcuts import render
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

from rest_framework import serializers
from .serializers import *

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

return_data=[]

#Getting a project list
    #Get
class listProjects(APIView):
    def __getList__(self,request):
        proj_recs = projects.objects.all()
        reurn_data=[]
        for item in proj_recs:
            return_data.append({'project':item})
        ser=ProjectSerializer()
        return ser.data
    def get(self,request,format=None):
        return Response(self.__getList__(request))

#POST
class modifyProject(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,format=None):
        if request.user.has_perm('project.modify_project'):
            for items in request.data['projects']:
                proj = projects.objects.get(id=items)
                if not projects.objects.filter(project=proj,user=request.user):
                    newproj = projects.objects.create(project=proj,user=request.user)
            return Response(self.__getList__(request))
    def delete(self,request, format=None):
        if request.user.has_perm('project.modify_project'):
            proj = projects.objects.get(id=pk)
            proj.delete()
            return Response(proj)

#Get all role Types
class roleList(APIView):
    def __getList__(self,request):
        proj_recs = projectRoleTypes.objects.all()
        reurn_data=[]
        for items in proj_recs:
            return_data.append({'roleType':item})
        #ser=ProjectsSerializer(return_data,many=True)
    def get(self,request,format=None):
        return Response(self.__getList__(request))

#get one role from all the roles
class getRole(APIView):
    def __getObj__(self,request,pk):
        type_recs = projectRoleTypes.objects.filter(name=pk)
    def get(self,request,pk,format=None):
        return Response(self.__getObj__(request,pk))

#Create a new role
    #POST
class newProjectRole(APIView):

    def post(self,request,format=None):

        #TODO check for existance
        if request.user.has_perm('project.create_role'):
            newRole = projectRoles.objects.create(name=requests.data['name'],
                                                    roleType = requests.data['type'],
                                                    numHours = requests.data['hours'])
            ser=projectRoleSerializer(projectRoles.objects.filter(user=request.user),many=True)
            return ser.data
#GET
class getProjectRole(APIView):
    def __get_role__(self,request,pk):
        roles = projectRoles.objects.filter(name=pk)
    def get(self,request,pk,format=None):
        return Response(self.__get_role__(request,pk))
#list all the porjects
class listProjectRoles(APIView):
    def __getList__(self,request):
        proj_role_recs = projectRoles.objects.all()
        reurn_data=[]
        for items in proj_role_recs:
            return_data.append({'project':item})
        #ser=ProjectsSerializer(return_data,many=True)
    def get(self,request,format=None):
        if data['permissions']['project']['modify']:
            return Response(self.__getList__(request))
#Generates newPlaces
class newPlaces(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request,format=None):
        if request.user.has_perm('project.create_place'):
            for items in request.data['project_places']:
                place = projectPlaces.objects.get(id=items)
                if not projectPlaces.objects.filter(project=proj,user=request.user):
                    newproj = projectPlaces.objects.create(project=place,user=request.user)
        return Response(self.__getList__(request))
#Get a place with a given id
    #PUT modify a place
    #DELETE mark the record as disabled
class modifyProjectPlace(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self,request,pk,format=None):
        if request.user.has_perm('modify_place'):
            places=request.data['places']
            ser=projectPlaceSerializer(request.user,data=request.data,partial=True)

        if ser.is_valid():
            ser.save()
            #login(request, user)
            return Response(ser.data)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        #check existance
        if request.user.has_perm('modify_place'):
            place = projectPlaces.objects.filter(name=pk,user=request.user)
            place.status = "Inactive"
            ser = projectPlaceSerializer(request.user,data=place)

        if ser.is_valid():
            ser.save()
            #login(request, user)
            return Response(ser.data)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

#Get a list of places
    #no arguments => places for a user
    #project_id => get all places for a project
    #project_role_id => give places for that id
class listPlaces(APIView):
    def __getUserPlacesList__(self,request):
        places = projectPlaces.objects.filter(user=request.user)
    def __getProjectPlacesList__(self,request):
        places = projectPlaces.objects.filter(project=request.project)
    def __getRolePlacesList__(self,request):
        places = projectPlaces.objects.filter(projectRole=request.role)
    def get(self,request,format=None):
        if (project in request):
            return(self.__getProjectPlacesList__(places))
        elif (project_role in request):
            return(self.__getRolePlacesList__(places))
        else:
            return(self.__getUserPlacesList__(places))
