from django.conf.urls import url
from .views import *

#Comes from API/pod/
urlpatterns = [
    url(r'^$',listProjects.as_view()),
    url(r'^(?P<pk>[0-9]+)$',modifyProject.as_view()),
    url(r'^roletypes/$',roleList.as_view()),
    url(r'^roletypes/(?P<pk>[0-9]+)$',getRole.as_view()),
    url(r'^projectrole/$',newProjectRole.as_view()),
    url(r'^projectrole/(?P<pk>[0-9]+)$',getProjectRole.as_view()),
    url(r'^projectroles/$',listProjectRoles.as_view()),
    url(r'^place/$',newPlaces.as_view()),
    url(r'^place/(?P<pk>[0-9]+)$',modifyProjectPlace.as_view()),
    url(r'^places/$',listPlaces.as_view()),
]