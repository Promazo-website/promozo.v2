from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^user/(?P<type>[^/]+)/$', userSkills.as_view()),
    url(r'^user/$',userSkills.as_view()),
    url(r'^skills/', newSkills.as_view()),
    url(r'^questions/$', Questions.as_view()),
    url(r'^answers/(?P<pk>[0-9]+)/$', questionsDetails.as_view()),
    url(r'^answers/$' ,questionsList.as_view()),

]
