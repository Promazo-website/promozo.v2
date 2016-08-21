from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from projects.models import ProjectRole
from application_tests.models import ApplicationTests, Question

# Create your models here.

class Application(models.Model):
    user = models.ForeignKey(User)
    role = models.ForeignKey(ProjectRole)
    attachedDoc = models.FileField(upload_to='application_docs/')
    cover_letter = models.TextField()
    status = models.CharField(default='Applied',max_length=20)

    def __str__(self):
        return "%s for %s" % (self.user.username, self.role.name)

class ApplicationNotes(models.Model):
    user = models.ForeignKey(User)
    application = models.ForeignKey(Application)
    created_on=models.DateTimeField(auto_now_add=True)
    note = models.TextField()

    def __str__(self):
        return "by: %s: for %s" % (self.user.username,self.application.user.username)

class AssignedTest(models.Model):
    role = models.ForeignKey(ProjectRole)
    test = models.ForeignKey(ApplicationTests)

    def __str__(self):
        return "test for role %s" % self.role.name

class ApplicantTestResults(models.Model):
    application =models.ForeignKey(Application, related_name="results_for")
    interviewer = models.ForeignKey(User, related_name="recorded_by")
    test = models.ForeignKey(AssignedTest)
    question = models.ForeignKey(Question)
    answer = models.TextField()

class ApplicationCases(models.Model):
    role = models.ForeignKey(ProjectRole)
    attachedDoc = models.FileField(upload_to='application_docs/')
    details = models.TextField()
    start_date = models.DateTimeField(blank=True,null=True)
    stop_date = models.DateTimeField(blank=True,null=True)

class ApplicationCaseResults(models.Model):
    application = models.ForeignKey(Application)
    case = models.ForeignKey(ApplicationCases)
    attachedDoc = models.FileField(upload_to='application_docs/')
    details = models.TextField()
    upload_date = models.DateTimeField(blank=True, null=True)
