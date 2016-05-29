from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url(r'^user/(?P<type>[^/]+)/$', userSkills.as_view()),
    url(r'^user/$',userSkills.as_view()),
    url(r'^skills/', newSkills.as_view()),
    url(r'^question/', QuestionAPI1.as_view())

]