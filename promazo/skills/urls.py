from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url(r'^user/$',userSkills.as_view()),
    url(r'^new/', newSkills.as_view()),
    url(r'^question/', QuestionAPI1.as_view())

]