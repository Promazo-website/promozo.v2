from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .UserRegistration import NewUserReg

User = get_user_model()

# Create your views here.
class userDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def user_type(self,user):
        if Student.objects.filter(user=user).exists():
            return 'student'
        elif BusinessUser.objects.filter(user=user).exists():
            return 'business'
        elif user.is_staff:
            return 'admin'
        else:
            return 'unknown'
    def get(self,request,format=None):
        """
        returns the current authenticated users details
        """
        ser=UserModelSerializer(request.user)
        return Response({'user_type':self.user_type(request.user),'record':ser.data})


class userLogin(APIView):

    permission_classes = (AllowAny,)

    def user_type(self,user):
        if Student.objects.filter(user=user).exists():
            return 'student'
        elif BusinessUser.objects.filter(user=user).exists():
            return 'business'
        elif user.is_staff:
            return 'admin'
        else:
            return 'unknown'
    def post(self,request,format=None):
        """
        This method allows users to be authenticated and logged into the system. It returns full data
        on the users record
        ---
        # YAML (must be separated by `---`)

        type:
          username:
            required: true
            type: string
          password:
            required: true
            type: password

        parameters:
            - name: username
              required: true
              type: string
            - name: password
              required: true
              paramType: string


        """
        if 'username' in request.data and 'password' in request.data:
            user = authenticate(username=request.data['username'],
                                password=request.data['password'])
            if user:
                login(request,user)
                ser=UserModelSerializer(user)
                return Response({'user_type':self.user_type(user),'record':ser.data})

            else:
                return Response('bad credentials', status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response('Bad data', status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,format=None):
        '''
        Logs a user out of the system

        Returns:

            done

        '''
        logout(request)
        return Response('done',status=status.HTTP_204_NO_CONTENT)

class UserRegistration(APIView):
    #todo create a base disabled user and send a verification email
    def __create_user__(self,request):
        try:
            newUser=User.objects.create(username=request.POST['username'],
                                        first_name=request.POST['first_name'],
                                        last_name=request.POST['last_name'],
                                        email=request.POST['email'],
                                        is_active=False)
            rec=NewUserReg()
            rec.GenerateUserEmail(newUser)
            return Response('Email sent', status=status.HTTP_200_OK)
        except:
            return Response('Error in User creation', status=status.HTTP_400_BAD_REQUEST)
        pass
    #todo verify the user and set password
    def __verify__(self,code1,code2):
        rec=NewUserReg()
        user=rec.verify_url(code1,code2)
        if type(user,User):
            ser=UserModelSerializer(user)
            return Response(ser.data)
        else:
            return Response('Bad verification URL')

    def __setPassword__(self,request,code1,code2):
        rec=NewUserReg()
        user=rec.verify_url(code1,code2)
        if type(user,User):
            user.set_password(request.post['password'])
            user.save()
            login(request,user)
            return Response('done')

        else:
            return Response('Bad verification URL')

    def post(self,request,type,code1=None,code2=None,format=None):
        """
        This request is used to create and verify a user into the system

        In the URL, you pass the type (create,verify) and if verify
        the two hash codes.

        The POST data is then used to create and/or activate the user
        """
        if type == 'create':
            return self.__create_user__(request)
        elif type == 'verify':
            return self.__verify__(request,code1,code2)
        elif type == 'setpassword':
            return self.__setPassword__(request,code1,code2)
        else:
            return Response('Bad request',status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,type):
        if type =='email':
            #todo check against universities to see if it is valid
            pass
        elif type == 'username':
            if User.objects.filter(username=request.get['username']).exists():
                return Response('Used')
            else:
                return Response('ok')
