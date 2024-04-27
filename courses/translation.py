from modeltranslation.translator import register, TranslationOptions
from .models import Course, Module, Content, Benefits, Teacher, \
             Testimonials, AskedQuestions, Resources


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'overview',)
    required_languages = ('ru', 'en')

@register(Module)
class ModuleTranslationOptions(TranslationOptions):
    fields = ('title', )
    required_languages = ('ru', 'en')

@register(Content)
class ContentTranslationOptions(TranslationOptions):
    fileds = ('title', 'description', )
    required_languages = ('ru', 'en')


@register(Benefits)
class BenefitsTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)
    required_languages = ('ru', 'en')


@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('position', 'body',)
    required_languages = ('ru', 'en')


@register(Testimonials)
class TestimonialsTranslationOptions(TranslationOptions):
    fields = ('name', 'body',)
    required_languages = ('ru', 'en')


@register(AskedQuestions)
class AskedQuestionsTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)
    required_languages = ('ru', 'en')


@register(Resources)
class ResourcesTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('ru', 'en')