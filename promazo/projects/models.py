from __future__ import unicode_literals

from django.db import models
from core.models import baseModel, userModel
from skills.models import skills
from pod.models import *
from django.contrib.auth.models import User

# Create your models here.

class statusField(models.Model):
    status = models.CharField(max_length=30, default='Active')

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

    def no_tasks(self):
        return ProjectTask.objects.filter(project=self).count()

    def no_roles(self):
        return ProjectRole.objects.filter(project=self).count()

    def no_places(self):
        return ProjectPlace.objects.filter(ProjectRole__project=self).count()

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

    A note here

    skillsRequired are a list of skills the owner states are must haves for a place
    skillsPrefered are a list of skills that are desireable
    skillsOptional are a list of skills that would be good to have
    """
    project = models.ForeignKey(Project)
    roleType = models.ForeignKey(ProjectRoleType)
    hours = models.IntegerField(default=0)
    skillsRequired = models.ManyToManyField(skills, related_name='skills_required', blank=True)
    skillsPrefered = models.ManyToManyField(skills, related_name='skills_prefered',blank=True)
    skillsOptional = models.ManyToManyField(skills, related_name='skills_optional',blank=True)

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
    note = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.ProjectRole.project.name