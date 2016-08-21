from django.conf.urls import url
from .views import *
from rest_framework import routers
#Comes from API/pod/

router= routers.DefaultRouter(trailing_slash=False)
router.register(r'roletypes',ProjectRoleTypeViewSet)
router.register(r'project', ProjectsViewSet)
router.register(r'projecttask', ProjectTaskViewSet)
router.register(r'projectrole', ProjectRoleViewSet)
router.register(r'projectplace', ProjectPlaceViewSet)

urlpatterns = router.urls