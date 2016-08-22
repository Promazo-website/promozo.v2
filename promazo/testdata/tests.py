from Factories import *
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


class AutoTestCase(TestCase):

    def setUp(self):
        self.testdata={}
        self.testdata['student_users'] = StudentUserModelFactory.create_batch(100)
        self.testdata['business_users'] = BusinessUserModelFactory.create_batch(20)
        self.testdata['university_users'] = UniversityUserFactory.create_batch(20)
        self.testdata['universities'] = UniversityFactory.create_batch(20)
        self.testdata['uni_emails'] = UniversityEmailFactory.create_batch(40)
        self.testdata['student_profiles'] = StudentFactory.create_batch(100)
        self.testdata['business_user_profile'] = BusinessUserProfileFactory.create_batch(20)
        self.testdata['businesses'] = BusinessFactory.create_batch(10)
        self.testdata['business_email'] = BusinessEmailFactory.create_batch(20)
        self.testdata['skills'] = SkillsFactory.create_batch(100)
        self.testdata['skill_scores'] = SkillScoresFactory.create_batch(400)
        self.testdata['skills_questions'] = SkillsQuestionFactory.create_batch(100)
        self.testdata['skills_q_answers'] = SkillsQuestionAnswersFactory.create_batch(300)
        self.testdata['skill_q_actions'] = SkillsQuestionAnswerActionsFactory.create_batch(400)
        self.testdata['questions'] = QuestionFactory.create_batch(100)
        self.testdata['tests'] = ApplicationTestsFactory.create_batch(20)
        self.testdata['pod_permissions'] = PodPermissionsFactory.create_batch(15)
        self.testdata['pod_roles'] = PodRolesFactory.create_batch(10)
        self.testdata['pods'] = PodFactory.create_batch(10)
        self.testdata['pod_members'] = PodMembersFactory.create_batch(30)
        self.testdata['project_roletypes'] = ProjectRoleTypeFactory.create_batch(5)
        self.testdata['projects'] = ProjectFactory.create_batch(20)
        self.testdata['project_tasks'] = ProjectTasksFactory.create_batch(100)
        self.testdata['project_roles'] = ProjectRoleFactory.create_batch(50)
        self.testdata['project_places_free'] = ProjectPlaceFreeFactory.create_batch(100)
        self.testdata['project_places_taken'] = ProjectPlaceTakenFactory.create_batch(100)
        self.testdata['applications'] = ApplicationFactory.create_batch(100)
        self.testdata['application_notes'] = ApplicationNotesFactory.create_batch(200)
        self.testdata['assigned_tests'] = AssignedTestsFactory.create_batch(100)
        self.testdata['application_test_results'] = ApplicationTestResultsFactory.create_batch(300)
        self.testdata['application_cases'] = ApplicationCasesFactory.create_batch(100)
        self.testdata['application_case_results'] = ApplicationCaseResultsFactory.create_batch(50)









    def test_adhoc(self):
        pass