from django.contrib import admin
from .models import Banner, Content, Ourpartners, Community, Module, Course, Subject, Teacher, Benefits, \
                    Testimonials, AskedQuestions, Resources

# Register your models here.

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['images']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Ourpartners)
class OurpartnersAdmin(admin.ModelAdmin):
    list_display = ['images', ]

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ['video', ]

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['module', 'title', 'description', 'content_type', 'item']


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
