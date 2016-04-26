from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url(r'^user/details/$',userDetails.as_view()),
    url(r'^user/login/',userLogin.as_view()),
    url(r'^user/registration/(?P<type>[^/]+)/$',UserRegistration.as_view()),
    url(r'^user/registration/(?P<type>[^/]+)/(?P<code1>[^/]+)/(?P<code2>[^/]+)/$',UserRegistration.as_view()),

]