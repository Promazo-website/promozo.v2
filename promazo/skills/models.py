from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
# Create your models here.

from core.models import baseModel

class skills(baseModel):
    """
    This model holds a list of skills that a user can have.
    'name' represents the name of the skill
    'type' currently relates to typeA ir typeB. The concept is that
    we need users to be able to add new skills to the system, but these must
    be verified, thus TypeB skills are ones added by the users, but not verified
    They cannot be scored in the system.
    TypeA are skills that can be scored, verified and add to the users GPA.

    A TypeB skill can be upgraded to a TypeA

    """
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=20,default='TypeB')

    def __str__(self):
        return self.name

class skillScores(baseModel):
    """
    Scores for each skill for a given user. Some of these will be altered by the user
    answering questions, but others will be set manually by admin users of various sorts
    A user is considered validated for a given skill if their score for that skill is over **%
    """
    user = models.ForeignKey(User, related_name='user_skills')
    skill = models.ForeignKey(skills)
    score = models.IntegerField(default=0)

    def __str__(self):
        return "%s - %s" % (self.user.username, self.skill.name)


class skillQuestion(baseModel):
    question = models.TextField()

    def answers(self):
        return skillQuestionAnswers.objects.filter(question=self)


class skillQuestionAnswers(baseModel):
    question = models.ForeignKey(skillQuestion)
    Answer = models.TextField()

    def actions(self):
        return skillQuestionAnswerAction.objects.filter(answer=self)

class skillQuestionAnswerAction(baseModel):
    answer = models.ForeignKey(skillQuestionAnswers)
    skill = models.ForeignKey(skills)
    ChangeToScore = models.IntegerField(default=0)

class userSkillAnswers(models.Model):
    user = models.ForeignKey(User)
    answer = models.ForeignKey(skillQuestionAnswers)
    created = models.DateTimeField(auto_now_add=True)

    def allAnswers(self):
        return skillQuestionAnswers.objects.filter(question=self.answer.question)
    def question(self):
        return self.answer.question
