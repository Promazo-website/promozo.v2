from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url(r'^user/details/$',userDetails.as_view()),
    url(r'^user/login/',userLogin.as_view()),
    url(r'^user/registration/(?P<type>[^/]+)/$',UserRegistration.as_view()),
    url(r'^user/registration/(?P<type>[^/]+)/(?P<code1>[^/]+)/(?P<code2>[^/]+)/$',UserRegistration.as_view()),
    url(r'^user/student/(?P<pk>[0-9]+)/$', StudentDetails.as_view()),
    url(r'^user/business/(?P<pk>[0-9]+)/$', BusinessUserDetails.as_view()),
    url(r'^user/avatar/$', UserAvatar.as_view()),
    url(r'^user/documents/$', UserDocumentationDetails.as_view()),
    url(r'^user/documents/(?P<pk>[0-9]+)/$', UserDocumentationDetails.as_view()),
]