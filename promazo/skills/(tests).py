from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your tests here.
class SkillsTestCase(TestCase):
    """
    Tests for the base User record
    """
    fixtures = ['testdata']

    def setUp(self):
        self.business_user = APIClient()
        self.business_user.login(username='testbusiness',password='test1234')
        self.student_user = APIClient()
        self.student_user.login(username='teststudent',password='test1234')

    def test_assignskill(self):
        #user assigns a TypeA skill to themselves
        resp=self.student_user.post('/api/skills/user/', {'skills':[1,2]})
        self.assertEqual(resp.status_code,200)
        self.assertContains(resp,'"assigned":true')
        self.assertContains(resp,'"assigned":false')
        self.assertContains(resp,'"validated":false')
    def test_removeSkill(self):
        #a user removes a skill assigned to them assuming the skill is scored at 0, or a TypeB skill
        resp=self.student_user.delete('/api/skills/user/', {'skills':[4]})
        self.assertEqual(resp.status_code,200)
        self.assertContains(resp,'"assigned":true')
        self.assertContains(resp,'"assigned":false')
        self.assertContains(resp,'"validated":false')
    def test_newSkill(self):
        resp = self.student_user.post('/api/skills/new/', {'name':'testing'})
        self.assertContains(resp,'"name":"testing","type":"TypeB"')
        #A user creates a new Skill that should be saved as a typeB skill
    def test_getSkills(self):
        #get a list of all skills, with types, if they are assigned to the user, validated status, and score
        resp =  self.student_user.get('/api/skills/user/')
        self.assertContains(resp,'"assigned":true')
        self.assertContains(resp,'"assigned":false')
        self.assertContains(resp,'"validated":false')
    def test_getQuestion(self):
        #get a skills question that the user has not answered
        resp = self.student_user.get('/api/skills/question/')
        self.assertContains(resp,'"answers":')
        self.assertContains(resp,'"actions":')
        #record an answer to a question
    def test_answerQuestion(self):
        resp =self.student_user.post('/api/skills/question/',{'answer':'3'})
        self.assertContains(resp,'"ChangeToScore":10')
