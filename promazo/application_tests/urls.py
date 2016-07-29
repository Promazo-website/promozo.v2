from django.conf.urls import url
from .views import *

# Comes from API/pod/
urlpatterns = [
    url(r'^question/$', QuestionList.as_view()),
    url(r'^question/(?P<pk>\d+)/$', QuestionDetails.as_view()),
    url(r'^tests/$', ApplicationTestList.as_view()),
    url(r'^tests/(?P<pk>\d+)/$', ApplicationTestDetails.as_view()),

]
