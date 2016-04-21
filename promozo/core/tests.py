from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your tests here.
class UserTestCase(TestCase):
    """
    Tests for the base User record
    """
    fixtures = ['testdata']

    def setUp(self):
        self.business_user = APIClient()
        self.business_user.login(username='testbusiness',password='test1234')
        self.student_user = APIClient()
        self.student.login(username='teststudent',password='test1234')

    #todo Get Current Users user details along with user Type and univeristy/business linked
    # to them assuming they are logged in

    def test_getUserDetailList(self):
        """
        This test should return a json object something like this form
        {
          'user_type': 'business/student/admin',
          'user_record' :
                            {
                             'id' @@ id of the user record
                             etc
                             'student' :
                                        {
                                        'id' : id of the student record if a student
                                        etc
                                        }
                             'business' :
                                        {
                                        'id' : id of the businessUser record if a Business User
                                        etc
                                        'Business' : {business record}
                                        }
                            }
        }
        :return:
        """
        resp =  self.business_user.get('/api/core/user/details/')
        data=resp.json()
        self.assertTrue('user_type' in data)
        self.assertTrue('user_record' in data)
        self.assertTrue(data['user_type']=='admin')
        self.assertTrue('id'in data['user_record']['business'])
        self.assertTrue('Business'in data['user_record']['business'])
        resp =  self.student_user.get('/api/core/user/details/')
        data=resp.json()
        self.assertTrue('user_type' in data)
        self.assertTrue('user_record' in data)
        self.assertTrue(data['user_type']=='student')
        self.assertTrue('id'in data['user_record']['student'])
    def test_UserDetailsUnauthorised(self):
        #attempt to get the current users details when the user is not authenticated and logged in
        resp = self.business_user.get('/api/core/user/details/')
        self.assertContains(resp, 'not authorised',status_code=401)
        self.assertContains(resp,'error',status_code=401)
    def test_resetPaswordAuthenticated(self):
        #reset a users password for an authenitucated user
        payload = {'password':'newPassword'}
        resp=self.business_user.patch('/api/core/user/details/', payload)
        self.assertContains(resp,'password reset')

    def test_resetPasswordUnauthenticated(self):
        payload = {'email':'testbusiness@test.com'}
        #send a password reset email to an unauthenticated user with a valid email
        resp=self.student_user.post('/api/core/user/reset/', payload)
        self.assertContains(resp,'An email has been sent with a reset link')
    def test_resetPasswordInvalidEmail(self):
        #attempt to send a password reset email to a user with an invalid email
        payload = {'email':'bademail@test.com'}
        resp=self.student_user.post('/api/core/user/reset/', payload)
        self.assertContains(resp,'Sorry, Email not found',status_code=401)
    def test_registerNewStudent(self):
        #register a new student assuming their email is valid for one of the universities in the system
        #when creating the API create it with a dummy call to send the email.
        payload = {'first_name':'unitTest', 'last_name':'test01', 'username':'test01',
                   'email':'test@valid.ac.com','password':'test0001'}
        resp = self.student_user.post('/api/core/user/details/', payload)
        self.assertContains(resp, 'Success')
    def test_registerInvalidStudent(self):
        #todo attempt to register a student with an invalid email
        payload = {'first_name':'unitTest', 'last_name':'test01', 'username':'test01',
                   'email':'test@invalid.ac.com','password':'test0001'}
        resp = self.student_user.post('/api/core/user/details/', payload)
        self.assertContains(resp, 'Invalid University email address')
    def test_login(self):
        payload = {'username':'testSstudent', 'password':'test1234'}
        #todo authenticate and log a user into the system with valid credentials
        c = APIClient()
        resp=c.post('/api/core/user/login/', payload)
        self.assertContains(resp,'user_type')
    def test_InvalidLogin(self):
        #todo attempt to authenticate a user with invalid credentials
        payload={'username':'testinvalid','password':'invalid'}
        c=APIClient()
        resp=c.post('/api/core/user/login/')
    def test_logout(self):
        #todo log the current user out of the system
        resp=self.student_user.delete('/api/core/user/login/')
        self.assertContains(resp,'Success')
    def test_modifyDetails(self):
        #todo modify a student users information
        payload = {'first_name':'Changed12'}
        resp=self.student_user.patch('/api/core/user/details/', payload)
        self.assertContains('Changed12')
    def test_failedModify(self):
        #todo attempt to modify a students details when the user is not authenticated
        payload = {'first_name':'Changed12'}
        c=APIClient()
        resp=c.patch('/api/core/user/details/', payload)
        self.assertEqual(resp.status_code,401)
    def test_changeBusinessUser(self):
        payload = {'first_name': 'Changed14' }
        resp=self.business_user.patch('/api/core/user/details/', payload)
        self.assertContains('Changed14')
    def test_listDocuments(self):
        resp=self.student_user.get('/api/core/user/documents/')
        self.assertContains(resp,'document1')
    def test_uploadDocument(self):
        file = open('testdata.json')
        payload={'name':'document1','document':file}
        resp= self.student_user.post('/api/core/user/documents/')
        self.assertContains(resp,'document1')
        self.assertContains(resp,'saved')
    def test_deleteDocument(self):
        resp = self.student_user.delete('/api/core/user/documents/1/')
        self.assertEqual(resp.status_code,204)