from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your tests here.

# Unit tests for projects portion
class UserTestCase(TestCase):
    #set up data
    def setUp(self):
        #set up test pks
        self.project_pk = '0'
        self.task_pk = '0'
        self.role_pk = '0'
        self.roletype_pk = '0'
        self.place_pk = '0'

        #Make anunauthenticated user
        self.student_user = APIClient()
        self.student_user.login(username='teststudent',password='test1234')


        #Make a user with super permissions for sending successful requests
        admin = User.objects.create_superuser(username='admin',email='',password='password')
        admin.save()

        self.super_user = APIClient()
        self.super_user.force_authenticate(user=admin)

    ## Project ##
    #GET /api/project/ should list all projects
    def test_getProjects(self):
        resp = self.super_user.get('/api/project/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(type(resp.json()),type([]))
    def test_getProjectsUnauthenticated(self):
        resp = self.student_user.get('/api/project/')
        self.assertEqual(resp.status_code,403)

    #GET /api/project/all should list all projects
    def test_getAllProjects(self):
        resp = self.super_user.get('/api/project/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(type(resp.json()),type([]))
    def test_getAllProjectsUnauthenticated(self):
        resp = self.student_user.get('/api/project/')
        self.assertEqual(resp.status_code,403)

    #GET /api/project/{pk} should get one specific project
    def test_getProject(self):
        resp = self.super_user.get('/api/project/'+self.project_pk+'/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(type(resp.json()),type({}))
    def test_getProjectUnauthenticated(self):
        resp = self.student_user.get('/api/project/'+self.project_pk+'/')
        self.assertEqual(resp.status_code,403)

    #GET /api/project/{pk}/users should return a list of users associated to one project
    def test_getProjectUsers(self):
        resp = self.super_user.get('/api/project/'+self.project_pk+'/users/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(type(resp.json()),type({}))
    def test_getProjectUsersUnauthenticated(self):
        resp = self.student_user.get('/api/project/'+self.project_pk+'/users/')
        self.assertEqual(resp.status_code,403)

    ## Project Tasks ##

    #GET /api/projecttask/ should list all tasks
    def test_getTasks(self):
        resp = self.super_user.get('/api/projecttask/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(type(resp.json()),type([]))
    def test_getTasksUnauthenticated(self):
        resp = self.student_user.get('/api/projecttask/')
        self.assertEqual(resp.status_code,403)

    #GET /api/projecttask/{pk} should return one project obj
    def test_getTask(self):
        resp = self.super_user.get('/api/projecttask/'+self.task_pk+'/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(type(resp.json()),type({}))
    def test_getTaskUnauthenticated(self):
        resp = self.student_user.get('/api/projecttask/'+self.task_pk+'/')
        self.assertEqual(resp.status_code,403)

    #GET /api/projecttask/{pk}/project should return projects that feature that task
    def test_getTaskProjects(self):
        resp = self.super_user.get('/api/projecttask/'+self.task_pk+'/project/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(type(resp.json()),type([]))
    def test_getTaskProjectsUnauthenticated(self):
        resp = self.student_user.get('/api/projecttask/'+self.task_pk+'/project/')
        self.assertEqual(resp.status_code,403)

    ## Project Roles ##

    #GET /api/projectrole/ should list all roles
    def test_getRoles(self):
        resp = self.super_user.get('/api/projectrole/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(type(resp.json()),type([]))
    def test_getRolesUnauthenticated(self):
        resp = self.student_user.get('/api/projectrole/')
        self.assertEqual(resp.status_code,403)

    #GET /api/projectrole/{pk} should return one role
    def test_getRole(self):
        resp = self.super_user.get('/api/projectrole/'+self.role_pk+'/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(type(resp.json()),type({}))
    def test_getRoleUnauthenticated(self):
        resp = self.student_user.get('/api/projectrole/'+self.role_pk+'/')
        self.assertEqual(resp.status_code,403)

    #GET /api/projectrole/{pk}/project should return projects that have that role
    def test_getRoleProjects(self):
        resp = self.super_user.get('/api/projectrole/'+self.role_pk+'/project/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(type(resp.json()),type([]))
    def test_getRoleProjectsUnauthenticated(self):
        resp = self.student_user.get('/api/projectrole/'+self.role_pk+'/project/')
        self.assertEqual(resp.status_code,403)

    ## Project Role Types ##

    #GET /api/roletypes/ should list all role types
    def test_getRoletypes(self):
        resp = self.super_user.get('/api/roletypes/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(type(resp.json()),type([]))
    def test_getRoletypesUnauthenticated(self):
        resp = self.student_user.get('/api/roletypes/')
        self.assertEqual(resp.status_code,403)

    #GET /api/roletypes/{pk} should return one role-type object
    def test_getRoletype(self):
        resp = self.super_user.get('/api/roletypes/'+self.roletype_pk+'/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(type(resp.json()),type([]))
    def test_getRoletypeUnauthenticated(self):
        resp = self.student_user.get('/api/roletypes/'+self.roletype_pk+'/')
        self.assertEqual(resp.status_code,403)

    ## Project Places ##

    #GET /api/projectplace/ should list all Places
    def test_getPlaces(self):
        resp = self.super_user.get('/api/projectplace/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(type(resp.json()),type([]))
    def test_getPlacesUnauthenticated(self):
        resp = self.student_user.get('/api/projectplace/')
        self.assertEqual(resp.status_code,403)

    #GET /api/projectplace/{pk} should return one place
    def test_getPlace(self):
        resp = self.super_user.get('/api/projectplace/'+self.place_pk+'/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(type(resp.json()),type({}))
    def test_getPlaceUnauthenticated(self):
        resp = self.student_user.get('/api/projectplace/'+self.place_pk+'/')
        self.assertEqual(resp.status_code,403)

    #GET /api/projectplace/{pk}/role











##Original test specs
    ##Project attributes

    #GET /api/project list of projects assigned to a user


    #POST /api/project Create a new project (pod users only)

    # PATCH /api/project/{pk}/ to update a project
    # PUT /api/project/{pk}/ to update a project
    #DELETE /api/project/{pk}/ to remove the project





    ## Project Role types

    #GET from /api/project/roletype/ a full list of role types

    #GET /api/project/roletype/{pk} the single pk record


    ## Project Roles

    #POST to /api/project/projectrole/ and create a role with a given project_id (only for pod managers)

    #GET to /api/project/projectroles/ and return a whole  list assigned to user
    #GET /api/project/projectroles/ with a project_id and return a single object

    #PATCH /api/project/projectrole/{pk} modify a specific project role
    #DELETE /api/project/projectrole/{pk} remove a project


    ## Project Places

    # POST /api/project/place/ to create a new place within project_role_id

    #GET /api/project/places/ return places for a user with no arguments
    #GET /api/project/places/ takes project_id and returns places for the project
    #GET /api/project/places/ takes project_role_id give the places for that id

    #PATCH /api/project/place/{pk} modify a specific rpoject place
    #DELETE /api/project/place/{pk} don't delete the project place, but do mark it as disabled
