from django.conf.urls import url
from .views import *

#Comes from API/pod/
urlpatterns = [
    url(r'^roletypes/$', ProjectRoleTypeList.as_view()),
    url(r'^roletypes/(?P<pk>\d+)/$', ProjectRoleTypeDetails.as_view()),
    url(r'^project/$',ProjectList.as_view()),
    url(r'^project/(?P<pk>\d+)/$', ProjectDetails.as_view()),
    url(r'^project/task/$', ProjectTaskList.as_view()),
    url(r'^project/task/(?P<pk>\d+)/$', ProjectTaskDetails.as_view()),
    url(r'^project/role/$', ProjectRoleList.as_view()),
    url(r'^project/role/(?P<pk>\d+)/$', ProjectRoleDetails.as_view()),
    url(r'^project/place/$', ProjectPlaceList.as_view()),
    url(r'^project/place/(?P<pk>\d+)/$', ProjectPlaceDetails.as_view()),
    
]
