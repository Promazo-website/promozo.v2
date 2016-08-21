from django.shortcuts import render

# Create your views here.
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

class ApplicationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    @list_route()
    def all(self,request):
        queryset=Application.objects.filter(user=request.user)
        ser=ApplicationSerializer(queryset, many=True)
        return Response(ser.data)
    @detail_route(methods=['GET'])
    def role(self,request,pk):
        queryset = Application.objects.filter(role__id=pk)
        ser = ApplicationSerializer(queryset, many=True)
        return Response(ser.data)

class ApplicationNotesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationNotesSerializer
    queryset = ApplicationNotes.objects.all()
    @detail_route(methods=['GET'])
    def application(self,request,pk):
        queryset=ApplicationNotes.objects.filter(application_id=pk)
        ser=ApplicationNotesSerializer(queryset,many=True)
        return Response(ser.data)

class AssignedTestViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AssignedTestsSerializer
    queryset = AssignedTest.objects.all()
    @detail_route(methods=['Get'])
    def role(self,request,pk):
        ser=AssignedTestsSerializer(AssignedTest.objects.filter(role__id=pk), many=True)
        return Response(ser.data)

class ApplicantTestResultsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicantTestResultsSerializer
    queryset = ApplicantTestResults.objects.all()
    @detail_route(methods=['GET'])
    def application(self,request,pk):
        ser=ApplicantTestResultsSerializer(ApplicantTestResults.objects.filter(applicant__id=pk),
                                           many=True)
        return Response(ser.data)


class ApplicationCasesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationCasesSerializer
    queryset = ApplicationCases.objects.all()
    @detail_route(methods=['GET'])
    def role(self,request,pk):
        queryset=ApplicationCases.objects.filter(role__id=pk)
        ser =  ApplicationCasesSerializer(queryset, many=True)
        return Response(ser.data)


class ApplicationCaseResultsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationCaseResultsSerializer
    queryset = ApplicationCaseResults.objects.all()
    @detail_route(methods=['GET'])
    def application(self,request,pk):
        queryset = ApplicationCaseResults.objects.filter(application__id=pk)
        ser = ApplicationCaseResultsSerializer(queryset, many=True)
        return Response(ser.data)
    @detail_route(methods=['GET'])
    def case(self,request,pk):
        queryset = ApplicationCaseResults.objects.filter(case__id=pk)
        ser = ApplicationCaseResultsSerializer(queryset, many=True)
        return Response(ser.data)
