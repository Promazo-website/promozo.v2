from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectRoleType)
admin.site.register(ProjectTask)
admin.site.register(ProjectRole)
admin.site.register(ProjectPlace)