from rest_framework import serializers
from .models import Banner, Ourpartners, Community, Subject, Content, Course, Module, Teacher, Benefits, \
                    Testimonials, AskedQuestions, Resources

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class OurpartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ourpartners
        fields = '__all__'


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class BenefitsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Benefits
        fields = '__all__'

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'

class AskedQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AskedQuestions
        fields = '__all__'

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'