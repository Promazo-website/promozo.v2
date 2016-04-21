from django.conf.urls import url,include
from .views import *

urlpatterns = [
#    url(r'^user/details/$',userLogin.as_view()),
#    url(r'^user/reset/$',userLogin.as_view()),
    url(r'^user/login/',userLogin.as_view()),
#    url(r'^user/documents/$',userLogin.as_view()),
#    url(r'^verifyuser/(?P<DateHash>[^/]+)/(?P<UserHash>[^/]+)/$',VerifyUser.as_view()),
#    url(r'^verifyreset/(?P<DateHash>[^/]+)/(?P<UserHash>[^/]+)/$',VerifyReset.as_view()),
]