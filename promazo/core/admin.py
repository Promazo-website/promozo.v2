from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(UserDocuments)
admin.site.register(University)
admin.site.register(Region)
admin.site.register(UniversityEmailFormats)
admin.site.register(Business)
admin.site.register(BusinessUser)
admin.site.register(BusinessEmailFormats)