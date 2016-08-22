import factory
from django.contrib.auth.models import User
from application_tests.models import *
from core.models import *
from pod.models import *
from projects.models import *
from skills.models import *
from applications.models import *
import datetime
import factory.fuzzy

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    first_name = factory.sequence(lambda n: 'First%03d' % n)
    last_name = factory.sequence(lambda n: 'Last%03d' % n)
    username = factory.sequence(lambda n: 'user_%d' % n)
    email = factory.LazyAttribute(lambda q: '%s@wtest_getcvx.com' % q.username)
    password ='user1234'


class StudentUserModelFactory(UserFactory):
    username = factory.sequence(lambda  n: 'student_%d' % n)

class BusinessUserModelFactory(UserFactory):
    username = factory.sequence(lambda  n: 'business_%d' % n)


class UniversityUserFactory(UserFactory):
    username = factory.sequence(lambda  n: 'university_%d' % n)

class UniversityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = University
    name  = factory.sequence(lambda n: 'University%03d' % n)
    logo = factory.django.ImageField(color='blue')
    description = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse massa tellus,
    suscipit quis sodales eget, luctus eget neque. Duis ultricies urna at libero posuere, id rutrum odio ultrices.
    Vestibulum erat mauris, aliquet quis lectus ac, ornare blandit nunc. Donec eleifend gravida orci in efficitur.
    Aliquam tempus orci eu est blandit aliquet. Proin malesuada odio ut dui blandit lobortis.
    Curabitur in enim porttitor, convallis augue ut, viverra neque.
    """
    website= "https://test.url.com"
    address = factory.LazyAttribute(lambda n: ' Address for %s' % n.name)
    @factory.post_generation
    def universityStaff(self, create, extracted, **kwargs):
        if create:
            self.universityStaff.add(User.objects.filter(username__istartswith='uni').order_by('?').first())
            self.universityStaff.add(User.objects.filter(username__istartswith='uni').order_by('?').first())
            self.universityStudents.add(User.objects.filter(username__istartswith='stu').order_by('?').first())
            self.universityStudents.add(User.objects.filter(username__istartswith='stu').order_by('?').first())

class UniversityEmailFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UniversityEmailFormats
    university =  factory.Iterator(University.objects.all())
    format =  factory.sequence(lambda n: 'email%03d@testUni.com' % n)

class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student
    user = factory.Iterator(User.objects.filter(username__istartswith="student"))
    address = factory.LazyAttribute(lambda q: 'Address for %s' % q.user.username)
    tagline = factory.LazyAttribute(lambda q: 'Tag line for %s' % q.user.username)
    description = factory.LazyAttribute(lambda q: 'Description for %s' % q.user.username)
    avatarImage = factory.django.ImageField(color='black')

class BusinessUserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BusinessUser
    user = factory.Iterator(User.objects.filter(username__istartswith="business"))
    jobTitle = factory.LazyAttribute(lambda q: 'Job Title for %s' % q.user.username)
    department = factory.LazyAttribute(lambda q: 'Department for %s' % q.user.username)
    tagline = factory.LazyAttribute(lambda q: 'Tag line for %s' % q.user.username)
    description = factory.LazyAttribute(lambda q: 'Description for %s' % q.user.username)
    avatarImage = factory.django.ImageField(color='black')

class BusinessFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Business
    name = factory.sequence(lambda n: 'Business%03d' % n)
    logo = factory.django.ImageField(color='blue')
    description = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse massa tellus,
    suscipit quis sodales eget, luctus eget neque. Duis ultricies urna at libero posuere, id rutrum odio ultrices.
    Vestibulum erat mauris, aliquet quis lectus ac, ornare blandit nunc. Donec eleifend gravida orci in efficitur.
    Aliquam tempus orci eu est blandit aliquet. Proin malesuada odio ut dui blandit lobortis.
    Curabitur in enim porttitor, convallis augue ut, viverra neque.
    """
    website = "https://test.url.com"
    address = factory.LazyAttribute(lambda n: ' Address for %s' % n.name)
    @factory.post_generation
    def Staff(self, create, extracted, **kwargs):
        if create:
            staff = User.objects.filter(username__istartswith='bus').order_by('?')
            self.staff.add(staff[0])
            self.staff.add(staff[1])
            self.staff.add(staff[2])
            self.staff.add(staff[3])
class BusinessEmailFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BusinessEmailFormats
    business =  factory.Iterator(Business.objects.all())
    format =  factory.sequence(lambda n: 'email%03d@testBus.com' % n)

class SkillsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = skills
    name =  factory.sequence(lambda n: 'skill%03d' % n)
    type = factory.fuzzy.FuzzyChoice(['TypeA','TypeB'])

class SkillScoresFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = skillScores
    user = factory.Iterator(User.objects.filter(username__istartswith="student"))
    skill = factory.Iterator(skills.objects.all())
    score = factory.fuzzy.FuzzyInteger(0,100)

class SkillsQuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = skillQuestion
    question = factory.sequence(lambda q: 'question__%03d' % q)

class SkillsQuestionAnswersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = skillQuestionAnswers
    question = factory.Iterator(skillQuestion.objects.all())
    Answer = factory.sequence(lambda q: 'Answer %03d' % q)

class SkillsQuestionAnswerActionsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model =skillQuestionAnswerAction
    answer = factory.Iterator(skillQuestionAnswers.objects.all())
    skill = factory.Iterator(skills.objects.all())
    ChangeToScore = factory.fuzzy.FuzzyInteger(-50,50)

class UserSkillAnswers(factory.django.DjangoModelFactory):
    class Meta:
        model = userSkillAnswers
    user = factory.Iterator(User.objects.filter(username__istartswith='student'))
    answer = factory.Iterator(skillQuestionAnswers.objects.all())

class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question
    question = factory.sequence(lambda q: 'Application Question %03d' % q)
    public = factory.fuzzy.FuzzyChoice([True,False])

class ApplicationTestsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ApplicationTests
    name = factory.sequence(lambda q: 'test %03d' % q)
    public = factory.fuzzy.FuzzyChoice([True,False])
    @factory.post_generation
    def questions(self, create, extracted, **kwargs):
        if create:
            qu=Question.objects.all().order_by('?')
            self.questions.add(qu[0])
            self.questions.add(qu[0])

class PodPermissionsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = podPermissions
    permission = factory.sequence(lambda q: 'permission %03d' % q)

class PodRolesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = podRole
    name = factory.sequence(lambda q: 'Pod Role %03d' % q)
    @factory.post_generation
    def permissions(self,create, extracted, **kwargs):
        if create:
            perms=podPermissions.objects.all().order_by('?')
            self.permissions.add(perms[0])
            self.permissions.add(perms[1])
            self.permissions.add(perms[2])


class PodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = pod
    name = factory.sequence(lambda  q: 'pod %03d' % q)

class PodMembersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = podMembers
    member = factory.Iterator(User.objects.filter(username__istartswith='bus'))
    pod = factory.Iterator(pod.objects.all())
    role = factory.Iterator(podRole.objects.all())

class ProjectRoleTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectRoleType
    name = factory.sequence(lambda q: 'Project RoleType %03d' % q)
    description = factory.LazyAttribute(lambda q: 'Project RoleType Description for %s ' % q.name)

class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project
    name = factory.sequence(lambda n: 'project_%03d' % n)
    status = factory.fuzzy.FuzzyChoice(['active','completed','suspended'])
    description = factory.LazyAttribute(lambda n: 'Description for : %s' % n.name)
    percentageCompleted = factory.fuzzy.FuzzyInteger(0,100)
    pod = factory.Iterator(pod.objects.all())


class ProjectTasksFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectTask
    name = factory.sequence(lambda n: 'project_Task_%03d' % n)
    status = factory.fuzzy.FuzzyChoice(['active', 'completed', 'suspended'])
    percentageCompleted = factory.fuzzy.FuzzyInteger(0, 100)
    project = factory.Iterator(Project.objects.all())

class ProjectRoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectRole
    name = factory.sequence(lambda n: 'Project Role_%03d' % n)
    project = factory.Iterator(Project.objects.all())
    roleType = factory.Iterator(ProjectRoleType.objects.all())
    hours = factory.fuzzy.FuzzyInteger(0,100)
    @factory.post_generation
    def skillsRequired(self,create, extracted, **kwargs):
        if create:
            sk=skills.objects.all().order_by('?')
            self.skillsRequired.add(sk[0])
            self.skillsRequired.add(sk[1])
            self.skillsRequired.add(sk[2])
            self.skillsPrefered.add(sk[3])
            self.skillsPrefered.add(sk[4])
            self.skillsPrefered.add(sk[5])
            self.skillsOptional.add(sk[6])
            self.skillsOptional.add(sk[7])
            self.skillsOptional.add(sk[8])

class ProjectPlaceFreeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectPlace
    startdate = factory.fuzzy.FuzzyDate(datetime.date.today(),datetime.date(2020,1,1))
    enddate = factory.fuzzy.FuzzyDate(datetime.date.today(), datetime.date(2020, 1, 1))
    ProjectRole = factory.Iterator(ProjectRole.objects.all())

class ProjectPlaceTakenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectPlace
    user = factory.Iterator(User.objects.filter(username__istartswith='stu'))
    startdate = factory.fuzzy.FuzzyDate(datetime.date.today(),datetime.date(2020,1,1))
    enddate = factory.fuzzy.FuzzyDate(datetime.date.today(), datetime.date(2020, 1, 1))
    ProjectRole = factory.Iterator(ProjectRole.objects.all())

class ApplicationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Application
    user = factory.Iterator(User.objects.filter(username__istartswith='stu'))
    role = factory.Iterator(ProjectRole.objects.all())
    attachedDoc = factory.django.FileField(filename='test.doc')
    cover_letter = factory.LazyAttribute(lambda n: 'Cover letter by student %s' % n.user.username)
    status = factory.fuzzy.FuzzyChoice(['Applied','Rejected','Accepted','Interview'])

class ApplicationNotesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ApplicationNotes
    user = factory.Iterator(User.objects.filter(username__istartswith='bus'))
    application = factory.Iterator(Application.objects.all())
    note = factory.LazyAttribute(lambda q: 'Application note for Application %d' % q.application.id)

class AssignedTestsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AssignedTest
    role = factory.Iterator(ProjectRole.objects.all())
    test = factory.Iterator(ApplicationTests.objects.all())

class ApplicationTestResultsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ApplicantTestResults
    test = factory.Iterator(AssignedTest.objects.filter(test__questions__isnull=False))
    application = factory.LazyAttribute(lambda n: Application.objects.filter(role=n.test.role).order_by('?').first())
    question = factory.LazyAttribute(lambda n: n.test.test.questions.all().order_by('?').first())
    answer = factory.LazyAttribute(lambda n: 'Answer to Question (%s)' % n.question.question)
    interviewer = factory.Iterator(User.objects.filter(username__istartswith='bus'))

class ApplicationCasesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ApplicationCases
    role = factory.Iterator(ProjectRole.objects.all())
    attachedDoc = factory.django.FileField(filename='case.doc')
    details = factory.LazyAttribute(lambda n: 'Details for Case attached to role %d' % n.role.id)
    start_date = factory.fuzzy.FuzzyDate(datetime.date.today(),datetime.date(2020,1,1))
    stop_date = factory.fuzzy.FuzzyDate(datetime.date.today(), datetime.date(2020, 1, 1))

class ApplicationCaseResultsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ApplicationCaseResults
    case = factory.Iterator(ApplicationCases.objects.all())
    application = factory.LazyAttribute(lambda n: Application.objects.filter(role=n.case.role).order_by('?').first())
    attachedDoc =factory.django.FileField(filename='caseResultsDoc.doc')
    upload_date = factory.fuzzy.FuzzyDate(datetime.date(2008, 1, 1))


def buildTestData():
    #StudentUserModelFactory.create_batch(100)
    #BusinessUserModelFactory.create_batch(20)
    #UniversityUserFactory.create_batch(20)
    #UniversityFactory.create_batch(20)
    #UniversityEmailFactory.create_batch(40)
    #StudentFactory.create_batch(100)
    #BusinessUserProfileFactory.create_batch(20)
    #BusinessFactory.create_batch(10)
    #BusinessEmailFactory.create_batch(20)
    #SkillsFactory.create_batch(100)
    #SkillScoresFactory.create_batch(400)
    #SkillsQuestionFactory.create_batch(100)
    #SkillsQuestionAnswersFactory.create_batch(300)
    #SkillsQuestionAnswerActionsFactory.create_batch(400)
    #QuestionFactory.create_batch(100)
    #ApplicationTestsFactory.create_batch(20)
    #PodPermissionsFactory.create_batch(15)
    #PodRolesFactory.create_batch(10)
    #PodFactory.create_batch(10)
    #PodMembersFactory.create_batch(30)
    #ProjectRoleTypeFactory.create_batch(5)
    #ProjectFactory.create_batch(20)
    #ProjectTasksFactory.create_batch(100)
    #ProjectRoleFactory.create_batch(50)
    #ProjectPlaceFreeFactory.create_batch(100)
    #ProjectPlaceTakenFactory.create_batch(100)
    #ApplicationFactory.create_batch(100)
    #ApplicationNotesFactory.create_batch(200)
    #AssignedTestsFactory.create_batch(100)
    ApplicationTestResultsFactory.create_batch(300)
    ApplicationCasesFactory.create_batch(100)
    ApplicationCaseResultsFactory.create_batch(50)
