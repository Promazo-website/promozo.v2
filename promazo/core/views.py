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
from rest_framework import generics

User = get_user_model()

class StudentDetails(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class BusinessUserDetails(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BusinessUserSerializer
    queryset = BusinessUser.objects.all()


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
    def put(self,request,format=None):
        '''
        Updates the current users user record

        args:

        * password
        * confirm_password (requried only if password is sent)
        * first_name
        * last_name

        Returns:

            User Details

        '''
        if 'password' in request.data:
            try:
                if not request.data['password'] == request.data['confirm_password']:
                    return Response("passwords are not the same",status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response("confirm_password was not found in form data", status=status.HTTP_400_BAD_REQUEST)
        ser=UserModelSerializer(request.user,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

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

    permission_classes = (AllowAny,)
    def __create_user__(self,request):
        newUser=User.objects.create(username=request.data['username'],
                                    first_name=request.data['first_name'],
                                    last_name=request.data['last_name'],
                                    email=request.data['email'],
                                    is_active=False)


        orgData=request.data['organisation']
        if request.data['type']=='University':
            Uni=University.objects.get(id=int(orgData['id']))
            studentRec=Student.objects.create(user=newUser,description="please fill in")
            Uni.universityStudents.add(newUser)
            Uni.save()

        else:
            business=Business.objects.get(id=int(orgData['id']))
            businessUser=BusinessUser.objects.create(user=newUser,description="please fill in")
            business.staff.add(newUser)
            business.save()
        rec=NewUserReg()
        rec.GenerateUserEmail(newUser)
        return Response('Email sent', status=status.HTTP_200_OK)
    def __verify__(self,request,code1,code2):
        rec=NewUserReg()
        user=rec.Verify_url(code1,code2)
        if isinstance(user,User):
            ser=UserModelSerializer(user)
            return Response(ser.data)
        else:
            return Response('Bad verification URL',status=status.HTTP_400_BAD_REQUEST)

    def __setPassword__(self,request,code1,code2):
        rec=NewUserReg()
        user=rec.Verify_url(code1,code2)
        if isinstance(user,User):
            user.set_password(request.data['password'])
            user.is_active = True
            user.save()
            return Response('done')

        else:
            return Response('Bad verification URL')
    def __resetPassword__(self,request):
        user=User.objects.filter(email=request.data['email'])
        if user.exists():
            rec=NewUserReg()
            rec.GenerateResetEmail(user[0])
            return Response('Done')
        else:
            return Response('not registered',status=status.HTTP_400_BAD_REQUEST)

    def post(self,request,type,code1=None,code2=None,format=None):
        """
        This request is used to create and verify a user into the system

        In the URL, you pass the type (create,verify) and if verify
        the two hash codes.

        The POST data is then used to create and/or activate the user
        """
        if type == 'create':
            return self.__create_user__(request)
        elif type =='requestreset':
            return self.__resetPassword__(request)
        elif type == 'verify':
            return self.__verify__(request,code1,code2)
        elif type == 'setpassword':
            return self.__setPassword__(request,code1,code2)
        else:
            return Response('Bad request',status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,type):
        if type =='email':
            if UniversityEmailFormats.objects.filter(format=request.GET['email'].split('@')[1]).exists() \
                    or BusinessEmailFormats.objects.filter(format=request.GET['email'].split('@')[1]).exists():
                return Response('ok')
            else:
                return Response('not Found', status=status.HTTP_406_NOT_ACCEPTABLE)
            pass
        if type =='organisation':
            if UniversityEmailFormats.objects.filter(format=request.GET['email'].split('@')[1]).exists():
                ser=UniversitySerializer(UniversityEmailFormats.objects.filter(format=request.GET['email'].split('@')[1])[0].university)
                return Response({'type':'University','organisation':ser.data})
            elif BusinessEmailFormats.objects.filter(format=request.GET['email'].split('@')[1]).exists():
                ser=BusinessSerializer(BusinessEmailFormats.objects.filter(format=request.GET['email'].split('@')[1])[0].business)
                return Response({'type':'Business','organisation':ser.data})
            else:
                return Response('not Found', status=status.HTTP_406_NOT_ACCEPTABLE)
            pass
        elif type == 'username':
            if User.objects.filter(username=request.GET['username']).exists():
                return Response('Used',status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response('ok')

class UserAvatar(APIView):
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
        if Student.objects.filter(user=request.user).exists():
            return Response({'avatar':Student.objects.get(user=request.user).avatarImage})
        elif BusinessUser.objects.filter(user=request.user).exists():
            return Response({'avatar':BusinessUser.objects.get(user=request.user).avatarImage})
        else:
            return Response('Not found',status=status.HTTP_400_BAD_REQUEST)
    def post(self,request,format=None):
        rec=False
        try:
            rec=Student.objects.get(user=request.user)
        except:
            try:
                rec=BusinessUser.objects.get(user=request.user)
            except:
                pass
        if rec:
            rec.avatarImage=request.data['file']
            rec.save()
            return Response({'avatar':rec.avatarImage.url})
        else:
            return Response('Not valid user',status=status.HTTP_400_BAD_REQUEST)


class UserDocumentationDetails(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,format=None):
        ser=UserDocumentsSerializer(UserDocuments.objects.filter(user=request.user),many=True)
        return Response(ser.data)

    def post(self,request,format=None):
        newRec=UserDocuments.objects.create(user=request.user,
                                            name=request.data['name'],
                                            document=request.data['document'])
        ser=UserDocumentsSerializer(UserDocuments.objects.filter(user=request.user),many=True)
        return Response(ser.data)
    def delete(self,request, pk,format=None):
        if UserDocuments.objects.filter(id=pk,user=request.user).exists():
            rec=UserDocuments.objects.get(id=pk)
            rec.delete()
            ser=UserDocumentsSerializer(UserDocuments.objects.filter(user=request.user),many=True)
            return Response(ser.data)
        else:
            return Response('Bad record',status=status.HTTP_400_BAD_REQUEST)

class BusinessCreate(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()

class UniversityCreate(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UniversitySerializer
    queryset = University.objects.all()