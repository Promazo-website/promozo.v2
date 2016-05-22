from django.contrib.admin import TabularInline, StackedInline, site
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin
from .models import *
# Register your models here.


class ActionsAdmin(SuperInlineModelAdmin,TabularInline):
    model=skillQuestionAnswerAction

class AnswersAdmin(SuperInlineModelAdmin,StackedInline):
    inlines = [ActionsAdmin,]
    model=skillQuestionAnswers

class QuestionAdmin(SuperModelAdmin):
    inlines = [AnswersAdmin]

site.register(skills)
site.register(skillQuestion,QuestionAdmin)
site.register(userSkillAnswers)
site.register(skillScores)