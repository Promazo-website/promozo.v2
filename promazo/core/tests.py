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
        #Logs in real generic user accounts
        self.business_user = APIClient()
        self.business_user.login(username='testbusiness',password='test1234')
        self.student_user = APIClient()
        self.student_user.login(username='teststudent',password='test1234')
        self.university_user = APIClient()
        self.university_user.login(username='testuniversity',password='test1234')

        #Logs in fake accounts that will have failed logins
        self.false_business_user = APIClient()
        self.false_business_user.login(username='fakebusiness',password='fake5678')
        self.false_student_user = APIClient()
        self.false_student_user.login(username='fakebusiness',password='fake5678')
        self.false_university_user = APIClient()
        self.false_university_user.login(username='fakeuniversity',password='fake5678')

    def test_getStudentDetailList(self):
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
        resp =  self.student_user.get('/api/core/user/details/')
        data=resp.json()
        self.assertTrue('user_type' in data)
        self.assertTrue('record' in data)
        self.assertTrue('id' in data[data.keys()[0]])
        self.assertTrue('student_details' in data[data.keys()[0]])

    def test_getBusinessDetailList(self):
        resp =  self.business_user.get('/api/core/user/details/')
        data=resp.json()
        self.assertTrue('user_type' in data)
        self.assertTrue('record' in data)
        self.assertTrue('id' in data[data.keys()[0]])
        self.assertTrue('Business' in data[data.keys()[0]])


    def test_getUniversityDetailList(self):
        resp =  self.university_user.get('/api/core/user/details/')
        data=resp.json()
        self.assertTrue('user_type' in data)
        self.assertTrue('record' in data)
        self.assertTrue('id' in data[data.keys()[0]])


    def test_getBusinessUserDetailsUnauthorised(self):
        #attempt to get the current users details when the user is not authenticated and logged in
        resp = self.false_business_user.get('/api/core/user/details/')
        self.assertTrue(resp.status_code==403)
    def test_getUniversityUserDetailsUnauthorised(self):
        #attempt to get the current users details when the user is not authenticated and logged in
        resp = self.false_university_user.get('/api/core/user/details/')
        self.assertTrue(resp.status_code==403)
    def test_getStudentUserDetailsUnauthorised(self):
        #attempt to get the current users details when the user is not authenticated and logged in
        resp = self.false_student_user.get('/api/core/user/details/')
        self.assertTrue(resp.status_code==403)


    #Tests the ability of an authenticated user
    def test_resetBusinessPaswordAuthenticated(self):
        #reset a users password for an authenitucated user
        payload = {'password':'newPassword', 'confirm_password':'newPassword'}
        resp = self.business_user.put('/api/core/user/details/', payload)
        self.assertEqual(resp.status_code,200)
    def test_resetStudentPaswordAuthenticated(self):
        #reset a users password for an authenitucated user
        payload = {'password':'newPassword', 'confirm_password':'newPassword'}
        resp = self.student_user.put('/api/core/user/details/', payload)
        self.assertEqual(resp.status_code,200)
    def test_resetUniversityPaswordAuthenticated(self):
        #reset a users password for an authenitucated user
        payload = {'password':'newPassword', 'confirm_password':'newPassword'}
        resp = self.university_user.put('/api/core/user/details/', payload)
        self.assertEqual(resp.status_code,200)


    #Tests existing accounts for password updates without authentication
    def test_businessResetPasswordUnauthenticated(self):
        payload = {'password':'newPassword', 'confirm_password':'newPassword'}
        #send a password reset email to an unauthenticated user with a valid email
        resp=self.false_business_user.put('/api/core/user/details/', payload)
        self.assertEqual(resp.status_code, 403)
    def test_studentResetPasswordUnauthenticated(self):
        payload = {'password':'newPassword', 'confirm_password':'newPassword'}
        #send a password reset email to an unauthenticated user with a valid email
        resp=self.false_student_user.put('/api/core/user/details/', payload)
        self.assertEqual(resp.status_code, 403)
    def test_universityResetPasswordUnauthenticated(self):
        payload = {'password':'newPassword', 'confirm_password':'newPassword'}
        #send a password reset email to an unauthenticated user with a valid email
        resp=self.false_university_user.put('/api/core/user/details/', payload)
        self.assertEqual(resp.status_code, 403)


    #Test the API to cange passwords when given a bad email
    #TODO: This could expand to all user types, but we need t get email validation working
    def test_registerNewUserInvalidEmail(self):
        #attempt to send a password reset email to a user with an invalid email
        payload = {'first_name':'unitTest', 'last_name':'test01', 'username':'test01',
                       'email':'test@invalid.ac.com','password':'test0001', 'confirm_password':'test0001'}
        resp=self.student_user.get('/api/core/user/registration/email/1234/12345')
        self.assertFalse(resp.status_code==200)


    #Register new users in each category

    def test_registerNewStudent(self):
        #register a new student assuming their email is valid for one of the universities in the system
        #when creating the API create it with a dummy call to send the email.
        payload = {'first_name':'unitTest', 'last_name':'test01', 'username':'test01',
                   'email':'test@valid.ac.com','password':'test0001', 'confirm_password':'test0001'}
        resp = self.student_user.put('/api/core/user/details/', payload)
        self.assertEqual(resp.status_code,200)
    def test_registerNewBusiness(self):
        #register a new student assuming their email is valid for one of the universities in the system
        #when creating the API create it with a dummy call to send the email.
        payload = {'first_name':'unitTest', 'last_name':'test01', 'username':'test01',
                   'email':'test@valid.ac.com','password':'test0001', 'confirm_password':'test0001'}
        resp = self.business_user.put('/api/core/user/details/', payload)
        self.assertEqual(resp.status_code,200)
    def test_registerNewUniversity(self):
        #register a new student assuming their email is valid for one of the universities in the system
        #when creating the API create it with a dummy call to send the email.
        payload = {'first_name':'unitTest', 'last_name':'test01', 'username':'test01',
                   'email':'test@valid.ac.com','password':'test0001', 'confirm_password':'test0001'}
        resp = self.university_user.put('/api/core/user/details/', payload)
        self.assertEqual(resp.status_code,200)

    def test_registerInvalidStudent(self):
        #todo attempt to register a student with an invalid email
        payload = {'first_name':'unitTest', 'last_name':'test01', 'username':'test01',
                   'email':'test@invalid.ac.com','password':'test0001', 'confirm_password':'test0001'}
        resp = self.student_user.get('/api/core/user/registration/email/1234/12345')
        self.assertFalse(resp.status_code == 200)
    '''
    #Test login for every type of user
    def test_student_login(self):
        self.student_user = APIClient()
        resp = self.student_user.login(username='teststudent',password='test1234')
        self.assertTrue(resp)
    def test_business_login(self):
        self.business_user = APIClient()
        resp = self.business_user.login(username='testbusiness',password='test1234')
        self.assertTrue(resp)
    def test_university_login(self):
        self.university_user = APIClient()
        resp = self.university_user.login(username='testuniversity',password='test1234')
        self.assertTrue(resp)
    '''
    #Test a generalized invalid login, everything is invalid. No need for specifics
    def test_InvalidBusinessLogin(self):
        #todo attempt to authenticate a user with invalid credentials
        self.false_business_user = APIClient()
        self.false_business_user.login(username='fakebusiness',password='fake5678')
    def test_InvalidStudentLogin(self):
        self.false_student_user = APIClient()
        self.false_student_user.login(username='fakebusiness',password='fake5678')
    def test_InvalidUniversityLogin(self):
        self.false_university_user = APIClient()
        self.false_university_user.login(username='fakeuniversity',password='fake5678')


    #Tests a logout for every single user class
    def test_student_logout(self):
        #todo log the current user out of the system
        resp=self.student_user.delete('/api/core/user/login/')
        #This is difficult to test, as the response returns nothing...
        self.assertEqual(resp.status_code,204)
    def test_business_logout(self):
        #todo log the current user out of the system
        resp=self.business_user.delete('/api/core/user/login/')
        #This is difficult to test, as the response returns nothing...
        self.assertEqual(resp.status_code,204)
    def test_university_logout(self):
        #todo log the current user out of the system
        resp=self.university_user.delete('/api/core/user/login/')
        #This is difficult to test, as the response returns nothing...
        self.assertEqual(resp.status_code,204)


    def test_modifyDetails(self):
        #todo modify a student users information
        payload = {'first_name':'Changed12'}
        resp=self.student_user.put('/api/core/user/details/', payload)
        self.assertContains(resp,'Changed12')

    #Tests modify with an account that isn't logged in
    def test_invalidModify(self):
        #todo attempt to modify a students details when the user is not authenticated
        payload = {'first_name':'Changed12'}
        c=APIClient()
        resp=c.put('/api/core/user/details/', payload)
        self.assertEqual(resp.status_code,403)

    #tests the ability to upload a document to a user

    def test_uploadDocument(self):
        file = open('test.json')
        payload={'name':'document1','document':file}
        resp= self.student_user.post('/api/core/user/documents/', payload)
        self.assertContains(resp,'document1')


    #Test the ability to list all documents attached to a student user
    def test_listDocuments(self):
        resp=self.student_user.get('/api/core/user/documents/')
        self.assertContains(resp,[]) #The test documents should remain blank
