from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your tests here.

# Unit tests for projects portion
class UserTestCase(TestCase):
    #set up data
    def setUp(self):
        #Make anunauthenticated user
        self.student_user = APIClient()
        self.student_user.login(username='teststudent',password='test1234')


        #Make a user with super permissions for sending successful requests
        admin = User.objects.create_superuser(username='admin',email='',password='password')
        admin.save()

        self.super_user = APIClient()
        self.super_user.force_authenticate(user=admin)


##Project attributes

#DELETE /api/project/{pk}/ to remove the project
# PATCH /api/project/{pk}/ to update a project
# PUT /api/project/{pk}/ to update a project

#GET list of projects assigned to a user
#POST Create a new project (pod users only)


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
