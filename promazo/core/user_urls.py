from django.conf.urls import url
from .views import *
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', UserViewSet)

urlpatterns = router.urls