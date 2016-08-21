from django.conf.urls import url
from .views import *
from rest_framework import routers

router= routers.DefaultRouter(trailing_slash=False)

router.register(r'applications',ApplicationViewSet)
router.register(r'applicationnotes', ApplicationNotesViewSet)
router.register(r'assignedtests',AssignedTestViewSet)
router.register(r'applicationtestresults',ApplicantTestResultsViewSet)
router.register(r'applicationcases', ApplicationCasesViewSet)
router.register(r'applicationcaseresults',ApplicationCaseResultsViewSet)

urlpatterns = router.urls