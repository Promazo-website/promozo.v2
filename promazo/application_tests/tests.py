from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        #Make anunauthenticated user
        self.student_user = APIClient()
        self.student_user.login(username='teststudent',password='test1234')


        #Make a user with super permissions for sending successful requests
        admin = User.objects.create_superuser(username='admin',email='',password='password')
        admin.save()

        self.super_user = APIClient()
        self.super_user.force_authenticate(user=admin)

    ## ALL should test authenticated or unauthenticated ##

    #GET /api/questions/ should list questions
    def test_getQuestionsList(self):
        resp = self.super_user.get('/api/questions')
        self.assertEqual(type(resp.json()), type([]))

    def test_getQuestionsListUnauthenticated(self):
        resp = self.student_user.get('/api/questions')
        self.assertEqual(resp.status_code,403)


    #GET /api/questions/all should reutrn all questions
    def test_getQuestionsAll(self):
        resp = self.super_user.get('/api/questions/all')
        self.assertEqual(type(resp.json()), type([]))

    def test_getQuestionsAllUnauthenticated(self):
        resp = self.student_user.get('/api/questions/all')
        self.assertEqual(resp.status_code,403)


    #GET /api/questions/{pk} should return one question(?)
    def test_getQuestion(self):
        pk = 'a'
        resp = self.super_user.get('/api/questions/'+pk)
        obj = resp.json()
        self.assertEqual(resp.status_code, 200)

    def test_getQuestionUnauthenticated(self):
        pk = 'a'
        resp = self.student_user.get('/api/questions/'+pk)
        self.assertEqual(resp.status_code,403)



    ## ALL should test authenticated or unauthenticated ##
    #GET /api/tests/ should list tests
    def test_getTestsList(self):
      resp = self.super_user.get('/api/tests')
      print resp
      self.assertEqual(type(resp.json()), type([]))

    def test_getTestsListUnauthenticated(self):
      resp = self.student_user.get('/api/tests')
      print resp
      self.assertEqual(resp.status_code,403)

    #GET /api/tests/all should list all questions
    def test_getTestsAll(self):
      resp = self.super_user.get('/api/tests/all')
      print resp
      self.assertEqual(type(resp.json()), type([]))

    def test_getTestsAllUnauthenticated(self):
      resp = self.student_user.get('/api/tests/all')
      print resp
      self.assertEqual(resp.status_code,403)


    #GET /api/tests/{pk} should return a specific test
    def test_getTest(self):
        pk = 'a'
        resp = self.super_user.get('/api/tests/'+pk)
        obj = resp.json()
        self.assertEqual(resp.status_code, 200)

    def test_getTestUnauthenticated(self):
        pk = 'a'
        resp = self.student_user.get('/api/tests/'+pk)
        self.assertEqual(resp.status_code,403)
