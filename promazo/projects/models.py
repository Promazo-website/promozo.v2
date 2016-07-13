from __future__ import unicode_literals

from django.db import models
from core.models import baseModel
from django.contrib.auth.models import User

# Create your models here.

#ProjectRoleType
class projectRoleTypes(baseModel):
    name = models.CharField(max_length=200)
    #There is no current part of the program that depends on this length limit, making it flexible
    def __str__(self):
        return self.name
####################################################
# Project Role
class projectRoles(baseModel):
    name = models.CharField(max_length=200)
    roleType = models.ForeignKey(projectRoleTypes)
    numHours = models.IntegerField() #there should not be hours estimates over 32767 hrs.
    def __str__(self):
        return self.name
####################################################
#Project Place
class projectPlaces(baseModel):
    name = models.CharField(max_length=200)
    projectRole = models.ManyToManyField(projectRoles,related_name="Is_a_part")
    userStartDate = models.DateField(auto_now=True,auto_now_add=False)
    endDate = models.DateField()
    #Setup Status options
    status = models.CharField(
        max_length = 50,
        choices = (
            ('Inactive','Inactive'),
            ('Active','Active')
        ),
        default='Active' #Upon creation, a place will probably be active
    )
    numHours = models.SmallIntegerField()
    notes = models.TextField()

    def __str__(self):
        return self.name
####################################################
#Project
class projects(baseModel):
    profile = models.ManyToManyField(User,related_name='Is_member',blank=True)
    roles = models.ForeignKey(projectRoles) #TODO, create a one_to_many
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
####################################################
#Project Tasks
class projectTasks(baseModel):
    project = models.OneToOneField(projects)
    taskName = models.CharField(max_length=200)
    #status = #TODO what is status? is it select or text field
    #PercentageCompleted #TODO, should we calculate or just enter a number

    def __str__(self):
        return self.taskName