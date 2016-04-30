from __future__ import unicode_literals

from django.db import models
from django_extensions.db.fields.json import JSONField
from django.contrib.auth.models import User
# Create your models here.

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

class UserDocuments(baseModel):
    """
    records used to store documents linked to a selected user
    """
    user =models.ForeignKey(User,related_name='document_owner')
    name = models.CharField(max_length=200)
    document = models.FileField(upload_to='userdocs')

    def __str__(self):
        return self.name

class University(baseModel):
    """
    Model for University Objects
    This includes links to University Staff and Students.
    Fields

    name : Charfield max 200 chars Required
    logo : Image field, uploaded to /images/logos/. Not Requried
    description : Text Field, Not Required
    address : text Field required
    universityStaff. M2M link to users
    universityStudents M2M link to Students
    """
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/logos',blank=True,null=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    address = models.TextField(blank=True)
    universityStaff = models.ManyToManyField(User,related_name='UniversityStaff',blank=True)
    universityStudents = models.ManyToManyField(User,related_name='UniversityStudents',blank=True)

    def __str__(self):
        return self.name

class Region(baseModel):
    """
    Region objects class linked to multiple universities
    """
    name = models.CharField(max_length=200)
    universities = models.ManyToManyField(University,related_name='universityRegion')
    RegionStaff = models.ManyToManyField(User,related_name='Region_Staff',blank=True)

    def __str__(self):
        return self.name

class UniversityEmailFormats(baseModel):
    """
    Lists of formats to be used to match a students email address
    with a university. If no match is found here, then the students
    request for a login will be rejected
    """
    university = models.ForeignKey(University,related_name='emailFormats')
    format = models.CharField(max_length=250)

    def __str__(self):
        return self.format

class Student(baseModel):
    """
    Student class holding basic information on the student
    """
    user = models.OneToOneField(User,related_name='student_details')
    address =models.TextField(null=True,blank=True)
    tagline = models.CharField(max_length=500,blank=True)
    description = models.TextField()
    avatarImage = models.ImageField(upload_to='images/avatars',null=True)
    settings = JSONField(blank=True,null=True)

    def __str__(self):
        return "%s(%s)" % (self.user.get_username(),self.user.get_full_name())

class BusinessUser(baseModel):
    """
    business user details
    """
    user = models.OneToOneField(User,related_name='business_user')
    jobTitle = models.CharField(max_length=200,blank=True,null=True)
    department = models.CharField(max_length=200,blank=True,null=True)
    tagline = models.CharField(max_length=500,blank=True)
    description = models.TextField()
    avatarImage = models.ImageField(upload_to='images/avatars',null=True)
    settings = JSONField(blank=True,null=True)

    def __str__(self):
        return self.user.username

class Business(baseModel):
    """
    object holding details on businesses in the system and
    which users are part of that business
    """
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='images/logos',null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    staff = models.ManyToManyField(User, related_name='business_staff',blank=True)

    def __str__(self):
        return self.name

class BusinessEmailFormats(baseModel):
    """
    Lists of formats to be used to match a business users email address
    with a business. If no match is found here, then they cannot sign up
    """
    business = models.ForeignKey(Business)
    format = models.CharField(max_length=250)

    def __str__(self):
        return self.format