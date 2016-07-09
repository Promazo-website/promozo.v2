from rest_framework import serializers
from .models import *

class ProjectRoleTypeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    #There is no current part of the program that depends on this length limit, making it flexible
    class Meta:
        model=projectRoleTypes()
####################################################
# Project Role
class ProjectRoleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    roleType = ProjectRoleTypeSerializer(read_only=True)
    numHours = serializers.IntegerField() #there should not be hours estimates over 32767 hrs.
    class Meta:
        model=projectRoles()
####################################################
#Project Place
class ProjectPlaceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    projectRole = ProjectRoleSerializer(read_only=True)
    userStartDate = serializers.DateField()
    endDate = serializers.DateField()
    status = serializers.CharField()
    numHours = serializers.IntegerField()
    notes = serializers.CharField()
    class Meta:
        model=projectPlaces()

####################################################
#Project
class ProjectSerializer(serializers.ModelSerializer):
    #TODO find user serializer
    #profile = serializers.ManyToManyField(User,related_name='Is_member',blank=True)
    roles = ProjectRoleSerializer(read_only=True,many=True)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField()
    class Meta:
        model=projects()
####################################################
#Project Tasks
class ProjectTaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    taskName = serializers.CharField(max_length=200)
    class Meat:
        model=projectTasks()
