from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import filters
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    filter_fields = ('user','public',)
    @list_route()
    def all(self, request):
        queryset=Question.objects.filter(user=request.user) | Question.objects.filter(public=True)
        ser=QuestionSerializer(queryset,many=True)
        return Response(ser.data)


class ApplicationTestsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationTestSerializer
    queryset = ApplicationTests.objects.all()
    filter_fields =('user','public','questions',)
    @list_route()
    def all(self,request):
        queryset=ApplicationTests.objects.filter(user=request.user) | ApplicationTests.objects.filter(public=True)
        ser=ApplicationTestSerializer(queryset,many=True)
        return Response(ser.data)

