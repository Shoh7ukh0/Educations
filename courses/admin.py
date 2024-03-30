from django.contrib import admin
from .models import Ourpartners, Community, Course, Lesson, Teacher, Benefits, \
                    Testimonials, AskedQuestions, Resources

# Register your models here.

@admin.register(Ourpartners)
class OurpartnersAdmin(admin.ModelAdmin):
    list_display = ['images', ]

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ['video', ]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', ]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'content', ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'body', ]


@admin.register(Benefits)
class BenefitsAdmin(admin.ModelAdmin):
    list_display = ['number', 'title', 'body',]


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['images', 'name', 'body', ]


@admin.register(AskedQuestions)
class AskedQuestionsAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', ]


@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', ]
