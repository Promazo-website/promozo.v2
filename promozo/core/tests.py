from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your tests here.
#todo Get Current Users user details along with user Type and univeristy/business linked to them assuming they are logged in
class UserTestCase(TestCase):
    """
    Tests for the base User record
    """
    fixtures = ['testdata']

    def setUp(self):
        self.admin_user = APIClient()
        self.admin_user.login(username='testadmin@test.com',password='test')
        self.student_user = APIClient()
        self.student.login(username='testcandidate@test.com',password='test')

    #create interviewset
    def test_createInterviewSet(self):
        payload={'name':'unit test added set', 'project':12,
                 'email_title':'unit test added set','email_text':'email body text from unit test',
                 'email_from':'unit test'}
        resp =  self.hr.post('/api/interviews/interviewset/', payload)
        self.assertContains(resp,'"name":"unit test added set"')
#todo attempt to get the current users details when the user is not authenticated and logged in
#todo reset a users password for an authenitucated user
#todo send a password reset email to an unauthenticated user with a valid email
#todo attempt to send a password reset email to a user with an invalid email
#todo register a new student assuming their email is valid for one of the universities in the system
#todo attempt to register a student with an invalid email
#todo authenticate and log a user into the system with valid credentials
#todo attempt to authenticate a user with invalid credentials
#todo log the current user out of the system
#todo modify a student users information
#todo attempt to modify a students details when the user is not authenticated
#todo modify a business users information
#todo for a business user, modify the business details
# todo for the current user, get a list of all their uploaded documentation
