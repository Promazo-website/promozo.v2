from microsite.views import *
from django.conf.urls import patterns, include, url

urlpatterns = [
                       url(r'^$', ProMazoHome, name='home'),
                       url(r'^how-it-works$', ProMazoHow, name='how-it-works'),
                       url(r'^how-it-works-student/$', ProMazoHowStudent, name='how-it-works-student'),
                       url(r'^student-stories$', StudentStories, name='student-stories'),
                       url(r'^stories/student-1$', Student1, name='student-1'),
                       url(r'^stories/student-2$', Student2, name='student-2'),
                       url(r'^stories/student-3$', Student3, name='student-3'),
                       url(r'^how-it-works-company$', ProMazoHowCompany, name='how-it-works-company'),
                       url(r'^corporate-work$', CorporateWork, name='corporate-work'),
                       url(r'^work/corporate-1$', Corporate1, name='corporate-1'),
                       url(r'^work/corporate-2$', Corporate2, name='corporate-2'),
                       url(r'^work/corporate-3$', Corporate3, name='corporate-3'),
                       url(r'^work/corporate-4$', Corporate4, name='corporate-4'),
                       url(r'^about$', About, name='about'),
                       url(r'^contact-us$', ContactUs, name='contact-us'),
                       url(r'^contact-pm$', ContactPM, name='contact-pm'),
                       url(r'^contact-send', ContactSend, name='contact-send'),
]