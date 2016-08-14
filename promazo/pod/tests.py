from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User

class UserTestCase(TestCase):
    # Create your tests here.
    def setUp(self):
        self.pod_pk = 'a' #The pk of our test comment
        self.permission_pk = 'a'

        #Make anunauthenticated user
        self.student_user = APIClient()
        self.student_user.login(username='teststudent',password='test1234')


        #Make a user with super permissions for sending successful requests
        admin = User.objects.create_superuser(username='admin',email='',password='password')
        admin.save()

        self.super_user = APIClient()
        self.super_user.force_authenticate(user=admin)

    ## ALL should test authenticated or unauthenticated ##

    #GET /api/pods/$ should produce a list of all pods
    def test_getPods(self):
        resp = self.super_user.get('/api/pods')
        self.assertTrue(resp.status_code, 200)
        self.assertEqual(type(resp.json()),type([]))

    def test_getPodsUnauthenticated(self):
        resp = self.super_user.get('/api/pods')
        self.assertTrue(resp.status_code, 403)

    #GET /api/pods/mypods/$ should return all pods associated with the user
    def test_getMyPods(self):
        resp = self.super_user.get('/api/pods/mypods')
        self.assertTrue(resp.status_code, 200)
        self.assertEqual(type(resp.json()),type([]))

    #GET /api/pods/{pk} should produce exactly one
    def test_getPod(self):
        resp = self.super_user.get('/api/pods/' + self.pod_pk)
        self.assertTrue(resp.status_code, 200)

    def test_getPodUnauthenticated(self):
        resp = self.super_user.get('/api/pods'+self.pod_pk)
        self.assertTrue(resp.status_code, 403)


    #GET /api/pods/{pk}/available-users should return list of users associated with that pod
    def test_getPodAvailableUsers(self):
        resp = self.super_user.get('/api/pods/' + self.pod_pk + '/available-users')
        self.assertTrue(resp.status_code, 200)

    def test_getPodAvailableUsersUnauthenticated(self):
        resp = self.super_user.get('/api/pods'+self.pod_pk+'/available-users')
        self.assertTrue(resp.status_code, 403)



    ## ALL should test authenticated or unauthenticated ##

    #GET /api/podmembers/{pk}/members should return all members of a pod
    def test_getPodMembers(self):
        resp = self.super_user.get('/api/pods/' + self.pod_pk + '/members')
        self.assertTrue(resp.status_code, 200)

    def test_getPodMembersUnauthenticated(self):
        resp = self.super_user.get('/api/pods'+self.pod_pk+'/members')
        self.assertTrue(resp.status_code, 403)




    ## ALL should test authenticated or unauthenticated ##

    #GET /api/podroles/ should list associated roles
    def test_getPodRoles(self):
        resp = self.super_user.get('/api/podroles')
        self.assertTrue(resp.status_code, 200)
        self.assertEqual(type(resp.json()),type([]))

    def test_getPodRolesUnauthenticated(self):
        resp = self.super_user.get('/api/podroles')
        self.assertTrue(resp.status_code, 403)


    #GET /api/podroles/{pk} should give details on one pod role
    def test_getPodRole(self):
        resp = self.super_user.get('/api/podroles')
        self.assertTrue(resp.status_code, 200)

    def test_getPodRoleUnauthenticated(self):
        resp = self.super_user.get('/api/podroles')
        self.assertTrue(resp.status_code, 403)




    ## ALL should test authenticated or unauthenticated ##

    #GET /api/podpermission/ should reutrn list of pod permissions
    def test_getPodPermissions(self):
        resp = self.super_user.get('/api/podpermission')
        self.assertTrue(resp.status_code, 200)
        self.assertEqual(type(resp.json()),type([]))

    def test_getPodRolesUnauthenticated(self):
        resp = self.super_user.get('/api/podpermission')
        self.assertTrue(resp.status_code, 403)

    #GET /api/podpermission/{pk} should return a single permission
    def test_getPodPermission(self):
        resp = self.super_user.get('/api/podpermission/'+self.permission_pk)
        self.assertTrue(resp.status_code, 200)

    def test_getPodRolesUnauthenticated(self):
        resp = self.super_user.get('/api/podpermission/'+self.permission_pk)
        self.assertTrue(resp.status_code, 403)
