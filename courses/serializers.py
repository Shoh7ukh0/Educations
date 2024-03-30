from rest_framework import serializers
from .models import Ourpartners, Community, Course, Lesson, Teacher, Benefits, \
                    Testimonials, AskedQuestions, Resources

class OurpartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ourpartners
        fields = '__all__'


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

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