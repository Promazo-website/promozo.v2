from django.test import TestCase
from django.test.client import Client
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

#TODO Set up a database that will contain valid test data

User=get_user_model()
# Create your tests here.
class SkillsTestCase(TestCase):
    #Test access a database fixture
    fixtures = ['testdata.json']
    '''
    Tests manipulating skills for the base user
    '''
    def setUp(self):
        self.business_user = APIClient()
        self.business_user.login(username='testbusiness',password='test1234')
        self.student_user = APIClient()
        self.student_user.login(username='teststudent',password='test1234')
        self.university_user = APIClient()
        self.university_user.login(username='testuniversity',password='test1234')


        self.admin = User.objects.create_superuser(username='aaaaa', email='test@test.com', password='pass')
        self.admin.save()

        self.student_user.force_authenticate(user=self.admin)
        #add one skill for testing
        self.skill = self.student_user.post('/api/skills/skills/', {'name':'testing'})


    # Check existance of skills
    def test_findSkill(self):
        resp = self.student_user.get('/api/skills/user/teststudent/')
        self.assertEqual(resp.status_code,200)

    #Check the addition of a new skill
    def test_newSkill(self):
        resp = self.student_user.post('/api/skills/skills/', {'name':'testing'})
        self.assertContains(resp,'"name":"testing","type":"TypeB"')
        #A user creates a new Skill that should be saved as a typeB skill

    #Try and remove a skill
    def test_removeSkill(self):
        #a user removes a skill assigned to them assuming the skill is scored at 0, or a TypeB skill
        resp=self.student_user.delete('/api/skills/user/', {'skills':1})
        self.assertEqual(resp.status_code,200)


    def test_assignskill(self):
        #user assigns a TypeA skill to themselves
        resp=self.student_user.post('/api/skills/user/', {'skills':[1,2]})
        self.assertEqual(resp.status_code,200)
        self.assertContains(resp,'"assigned":true')
        self.assertContains(resp,'"assigned":false')
        self.assertContains(resp,'"validated":false')

    def test_getQuestion(self):
        #get a skills question that the user has not answered
        resp = self.student_user.get('/api/skills/questions/',{'answer':1})
        self.assertContains(resp,'"answers":')
        self.assertContains(resp,'"actions":')
        #record an answer to a question

    def test_answerQuestion(self):
        resp =self.student_user.post('/api/skills/questions/',{'answer':1})
        self.assertContains(resp,'"ChangeToScore":10')
