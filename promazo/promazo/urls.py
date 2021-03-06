"""promozo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/docs/', include('rest_framework_swagger.urls')),
    url(r'^api/core/', include('core.urls')),
    url(r'^api/skills/', include('skills.urls')),
    url(r'^api/', include('core.user_urls')),
    url(r'^api/', include('pod.urls')),
    url(r'^api/',include('projects.urls')),
    url(r'^api/', include('application_tests.urls')),
    url(r'^api/', include('applications.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^validate/(?P<DateHash>[^/]+)/(?P<UserHash>[^/]+)/$', Verification),
    url(r'^promazo/$',Main),
    url(r'^', include('microsite.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
