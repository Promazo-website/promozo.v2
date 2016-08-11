from django.conf.urls import url
from .views import *
from rest_framework import routers
router= routers.DefaultRouter(trailing_slash=False)
router.register(r'resource',SkillsViewSet)
urlpatterns = [
    url(r'^user/(?P<type>[^/]+)/$', userSkills.as_view()),
    url(r'^user/$',userSkills.as_view()),
    url(r'^skills/', newSkills.as_view()),
    url(r'^questions/$', Questions.as_view()),
    url(r'^answers/(?P<pk>[0-9]+)/$', questionsDetails.as_view()),
    url(r'^answers/$' ,questionsList.as_view()),

] + router.urls
