from __future__ import unicode_literals

from django.db import models
from core.models import baseModel, userModel
from pod.models import *
from django.contrib.auth.models import User

# Create your models here.

class statusField(models.Model):
    status = models.CharField(max_length=30)

    class Meta:
        abstract = True

class nameField(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        abstract=True

class ProjectRoleType(nameField):
    """
    Records that define the different types of roles that can be assigned to a project
    """

    description=models.TextField()

    def __str__(self):
        return self.name


class Project(baseModel, statusField,nameField):
    """
    Base Project record
    """
    pod = models.ForeignKey(pod)
    description=models.TextField()
    percentageCompleted = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ProjectTask(baseModel,statusField,nameField):
    """
    subtasks assigned to a project
    """
    project = models.ForeignKey(Project)
    percentageCompleted = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ProjectRole(nameField,baseModel):
    """
    A job/position/role required by a project
    """
    project = models.ForeignKey(Project)
    roleType = models.ForeignKey(ProjectRoleType)
    hours = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ProjectPlace(statusField):
    """
    A record denoting the person who is assigned to a role in a project.
    Thus a role might be assigned to multiple people
    """
    user = models.ForeignKey(User, blank=True, null=True)
    startdate = models.DateField(blank=True,null=True)
    enddate = models.DateField(blank=True,null=True)
    ProjectRole = models.ForeignKey(ProjectRole)
    hours = models.IntegerField(default=0)
    note = models.TextField()

    def __str__(self):
        return "%s - %s" % (self.ProjectRole.project.name, self.user.username)