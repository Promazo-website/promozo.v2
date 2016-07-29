from django.shortcuts import render
from .models import *

from rest_framework import serializers
#from .serializers import *

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

#Getting a project list
    #Get
class listProjects(APIView):
    def __getList__(self,request):
        proj_recs = projects.objects.all()
        reurn_data=[]
        for items in proj_recs:
            return_data.append({'project':item})
        ser=ProjectsSerializer(return_data,many=True)
    def get(self,request,format=None):
        return Response(self.__getList__(request))
