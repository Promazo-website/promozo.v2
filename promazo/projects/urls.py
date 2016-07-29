from django.conf.urls import url
from .views import *

#Comes from API/pod/
urlpatterns = [
    url(r'^$',listProjects.as_view()),
    
]
