from django.contrib import admin
from .models import Our_partners, Community, Course, Lesson, Teacher, Benefits, \
                    Testimonials, Asked_Questions, Resources

# Register your models here.

@admin.register(Our_partners)
class Our_partnersAdmin(admin.ModelAdmin):
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


@admin.register(Asked_Questions)
class Asked_QuestionsAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', ]


@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', ]
