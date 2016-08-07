from .views import *
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'questions',QuestionViewSet, base_name='Questions')
router.register(r'tests', ApplicationTestsViewSet, base_name='ApplicationTests')

urlpatterns = router.urls
