from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class userModel(models.Model):
    user = models.ForeignKey(User,null=True)
    class Meta:
        abstract = True

class baseModel(models.Model):
    """
    This is an abstract model. No table is created for this, Instead it
    lists fields that are added to other models, based on this one
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User,null=True)

    class Meta:
        abstract=True

class Question(baseModel):
    question = models.TextField()
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.question

class ApplicationTests(baseModel):
    name = models.CharField(max_length=200)
    questions =models.ManyToManyField(Question)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name




