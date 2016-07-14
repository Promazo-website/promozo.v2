from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', podList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', podMemberList.as_view()),
    url(r'^user/$', userPodList.as_view()),
    url(r'^permissions/$', userHasPerm.as_view()),
]