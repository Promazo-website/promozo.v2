from __future__ import unicode_literals

from django.db import models
from core.models import baseModel
from django.contrib.auth.models import User

class podPermissions(baseModel):
    permission = models.CharField(max_length=200)

    def __str__(self):
        return self.permission

class podRole(baseModel):
    name = models.CharField(max_length=200)
    permssions = models.ManyToManyField(podPermissions)
    def __str__(self):
        return self.name

    def has_permission(self,permission):
        return self.permissions.filter(permission=permission).exists()

class pod(baseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def members_count(self):
        return podMembers.objects.filter(pod=self).count()

class podMembers(baseModel):
    member=models.ForeignKey(User,related_name='member_of')
    pod = models.ForeignKey(pod)
    role = models.ForeignKey(podRole,blank=True, null=True)

    def __str__(self):
        return "Pod(%s) Role(%s) User(%s)" % (self.pod.name, self.role.name, self.member.username)

    def permissions(self):
        return self.role.permissions.all()

    def has_permission(self,permission):
        return self.role.has_permission(permission)
