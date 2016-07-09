# Create your tests here.

from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User=get_user_model()
# Unit tests for projects portion

pk = '1234' #The project ID we will always use

class UserTestCase(TestCase):
  #NOTE: The structure for these tests has nothing to do with roles or ranks, we are relying solely on the PERMISSIONS being attached to the request
    #Permissions Are:
#       1. Create Project
#       2. Modify existing project
#       3. Create a role
#       4. Assign a role
#We identify each permission in a unique tag in the permissions portion of the request body
    #So any role will be defined by which of these permissions it has
#EXAMPLE Permissions objects
#{
#  permissions:{
#    pod:{
#        create:True,
#        modify:True
#    },
#    project:{
#        create:True,
#        modify:True
#    }
#  }
#}
    def setUp(self):
        #Logs in real generic user accounts
        self.student_user = APIClient()
        self.student_user.login(username='teststudent',password='test1234')

    ##Project attributes

    #GET /api/projects/ Should get a list of projects from an authenticated request
    def test_getProject(self):  #No added permissions required, get works on a logged in user
        resp = self.student_user.get('/api/projects/')
        self.assertEqual(resp.status_code,200)
    #DELETE /api/project/{pk}/ to remove the project
    #require modify project permission

    #First test an allowed delete
    def test_deleteProject_Authenticaed(self):
        resp = self.student_user.delete('/api/projects/1234',{'permissions':{'pod':{'modify':True}}})
        self.assertEqual(resp.status_code,200)
    #Now test without permissions
    def test_deleteProject_Unauthenticated
        resp = self.student_user.delete('/api/projects/1234',{'permissions':{'pod':{'modify':True}}})
        self.assertEqual(resp.status_code,404)

    # PATCH /api/project/{pk}/ to update a project
    # PUT /api/project/{pk}/ to update a project
    def test_updateProject_Authenticaed(self):
        resp = self.student_user.patch('/api/projects/'+pk,{'permissions':{'pod':{'modify':True}},'project':{}})
        self.assertEqual(resp.status_code,200)
    def test_updateProject_Unauthenticaed(self):
        resp = self.student_user.patch('/api/projects/1234',{'project':{}})
        self.assertEqual(resp.status_code,404)


    ## Project Role types

    #GET from /api/project/roletype/ a full list of role types
    #No authentication necessary

    def test_getAllRoles(self):
        resp = self.student_user.get('/api/projects/roletype/')
        self.assertEqual(resp.status_code,200)


    #GET /api/project/roletype/{pk} the single pk record
    def test_getOneRole(self):
        resp = self.student_user.get('/api/project/roletype/'+pk)
        self.assertEqual(resp.status_code,200)
    ## Project Roles

    #POST to /api/project/projectrole/ and create a role with a given project_id (only for pod managers)
    def test_newRole(self):
        resp = self.student_user.post('/api/project/projectrole/',{'permissions':{'project':{'modify':True}},'role':{}})
        self.assertEqual(resp.status_code,200)
    #PATCH /api/project/projectrole/{pk} modify a specific project role
    def test_modifyRoleAuthenticated(self):
        resp = self.student_user.patch('/api/project/projectrole/'+pk,{'permissions':{'project':{'modify':True}},'role':{}})
        self.assertEqual(resp.status_code,200)
    def test_modifyRoleUnauthenticated(self):
        resp = self.student_user.patch('/api/project/projectrole/'+pk,{'permissions':{},'role':{}})
        self.assertEqual(resp.status_code,404)

    #DELETE /api/project/projectrole/{pk} remove a project
    def test_deleteRoleAuthenticated(self):
        resp = self.student_user.patch('/api/project/projectrole/'+pk,{'permissions':{'project':{'modify':True}},'role':{}})
        self.assertEqual(resp.status_code,200)
    def test_deleteRoleUnauthenticated(self):
        resp = self.student_user.patch('/api/project/projectrole/'+pk,{'permissions':{},'role':{}})
        self.assertEqual(resp.status_code,404)


    #GET to /api/project/projectroles/ and return a whole  list assigned to user

    #GET /api/project/projectroles/ with a project_id and return a single object




    ## Project Places

    #GET /api/project/places/ return places for a user with no arguments
    def test_getAllPlaces(self):
        resp = self.student_user('/api/project/places/',{})
        self.assertEqual(resp.status_code,200)
    #GET /api/project/places/ takes project_id and returns places for the project
    def test_getAllPlaces(self):
        resp = self.student_user('/api/project/places/',{'project':''})
        self.assertEqual(resp.status_code,200)
    #GET /api/project/places/ takes project_role_id give the places for that id
    def test_getAllPlaces(self):
        resp = self.student_user('/api/project/places/',{'project_role':''})
        self.assertEqual(resp.status_code,200)


        
    # POST /api/project/place/ to create a new place within project_role_id
    def test_makeProjectPlace_Authenticated(self):
        resp = self.student_user.post('/api/project/place',{,'permissions':{'project':{'modify':True}},'place':{}})
        self.assertEqual(resp.status_code,200)
    def test_makeProjectPlace_Unauthenticated(self):
        resp = self.student_user.post('/api/project/place',{,'permissions':{},'place':{}})
        self.assertEqual(resp.status_code,404)

    #PATCH /api/project/place/{pk} modify a specific rpoject place
    def test_modifyProjectPlace_Authenticated(self):
        resp = self.student_user.post('/api/project/place/'+pk,{,'permissions':{'project':{'modify':True}},'place':{}})
        self.assertEqual(resp.status_code,200)
    def test_modifyProjectPlace_Unauthenticated(self):
        resp = self.student_user.post('/api/project/place/'+pk,{,'permissions':{},'place':{}})
        self.assertEqual(resp.status_code,404)

    #DELETE /api/project/place/{pk} don't delete the project place, but do mark it as disabled
    def test_deleteProjectPlace_Authenticated(self):
        resp = self.student_user.post('/api/project/place/'+pk,{,'permissions':{'project':{'modify':True}},'place':{}})
        self.assertEqual(resp.status_code,200)
    def test_deleteProjectPlace_Unauthenticated(self):
        resp = self.student_user.post('/api/project/place/'+pk,{,'permissions':{},'place':{}})
        self.assertEqual(resp.status_code,404)
