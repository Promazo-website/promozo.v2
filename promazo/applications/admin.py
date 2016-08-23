from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Application)
admin.site.register(ApplicationNotes)
admin.site.register(AssignedTest)
admin.site.register(ApplicantTestResults)
admin.site.register(ApplicationCases)
admin.site.register(ApplicationCaseResults)