from django.contrib import admin
from .models import Technologies, Question, Choice

# Register your models here.

@admin.register(Technologies)
class TechnologiesAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text', 'is_correct']