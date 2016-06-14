from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.

#list of pod members

class podMemberList(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = podMembersSerializer
    def get_queryset(self):
        return podMembers.objects.filter(pod__id=self.kwargs['pk'])

# list pods

class podList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = podSerializer
    queryset = pod.objects.all()

#list of user pods

class userPodList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = podSerializer
    def get_queryset(self):
        return [x.pod for x in podMembers.objects.filter(role__user=self.request.user)]

# has user permission * for pod *

class userHasPerm(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        try:
            return Response(podMembers.objects.get(pod__if=request.GET['pod'],user=request.user).has_permission(request.GET['permission']))
        except:
            return Response(False)
