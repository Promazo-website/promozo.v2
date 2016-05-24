from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import generics

User = get_user_model()

class userSkills(APIView):
    permission_classes = (IsAuthenticated,)

    def __getList__(self,request):
        skill_recs=skills.objects.all()
        return_data=[]
        for items in skill_recs:
            Assigned=False
            Validated=False
            userSkill=skillScores.objects.filter(user=request.user,skill=items)
            if userSkill.exists():
                Assigned=True
                if userSkill[0].score > 0:
                    Validated=True
            return_data.append({'skill':items,'assigned':Assigned,'validated':Validated})
        ser=UserSkillsSerializer(return_data, many=True)
        return ser.data
    def get(self,request,format=None):
        return Response(self.__getList__(request))

    def post(self,request,format=None):
        for items in request.data['skills']:
            skill=skills.objects.get(id=items)
            if not skillScores.objects.filter(skill=skill,user=request.user):
                newrec = skillScores.objects.create(skill=skill,user=request.user)
        return Response(self.__getList__(request))
    def delete(self,request,format=None):
        recs = skillScores.objects.filter(skill__id__in=request.data['skills'],user=request.user)
        if recs.exists():
            recs.delete()
            return Response(self.__getList__(request))
        else:
            return Response('No records', status=status.HTTP_400_BAD_REQUEST)


class newSkills(userSkills):
    permission_classes = (IsAuthenticated,)
    def post(self,request,format=None):
        if 'name' in request.data:
            newrec=skills.objects.create(name=request.data['name'],type='TypeB')
            newrec2=skillScores.objects.create(skill=newrec,user=request.user)
        return Response(self.__getList__(request))

class QuestionAPI1(APIView):
    permission_classes = (IsAuthenticated,)
    def __getQuestions__(self,request):
        answers = userSkillAnswers.objects.filter(user=request.user)
        ser = userSkillAnswersSerializer(answers,many=True)
        return ser.data
    def get(self,request,format=None):
        """
        Returns a list of unanswered skills questions
        """
        questions=skillQuestion.objects.all().exclude(id__in=userSkillAnswers.objects.filter(user=request.user).values_list('answer__question__id',flat=True))
        ser=skillQuestionsSerializer(questions,many=True)
        return Response(ser.data)
    def post(self,request,format=None):
        answer=skillQuestionAnswers.objects.get(id=request.data['answer'])
        user_answers = userSkillAnswers.objects.filter(user=request.user, answer__question=answer.question)
        if user_answers.exists():
            user_answers.delete()
        newRec=userSkillAnswers.objects.create(user=request.user, answer=answer)
        return Response(self.__getQuestions__(request))

