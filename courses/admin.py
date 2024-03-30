from django.contrib import admin
from .models import Course, Lesson, Teacher, Upcoming_Events, \
                    Readers_Opinion, Top_Products, Quick_Links, \
                    Features, Resources

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', ]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'content', ]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'body', ]

@admin.register(Upcoming_Events)
class Upcoming_EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'location', 'date', ]

@admin.register(Readers_Opinion)
class Readers_OpinionAdmin(admin.ModelAdmin):
    list_display = ['images', 'name', 'body', ]

@admin.register(Top_Products)
class Top_ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', ]

@admin.register(Quick_Links)
class Quick_LinksAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', ]

@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', ]

@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', ]