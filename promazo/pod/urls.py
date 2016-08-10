from django.conf.urls import url
from .views import *
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'pods', PodViewSet)
router.register(r'podmembers', PodMembersViewSet)
router.register(r'podroles', PodRolesViewSet)
router.register(r'podpermission', PodPermissionsViewSet)

urlpatterns = router.urls
