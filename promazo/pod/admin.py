from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(pod)
admin.site.register(podPermissions)
admin.site.register(podMembers)
admin.site.register(podRole)