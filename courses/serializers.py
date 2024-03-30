from rest_framework import serializers
from .models import Our_partners, Community, Course, Lesson, Teacher, Benefits, \
                    Testimonials, Asked_Questions, Resources

class Our_partnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_partners
        fields = '__all__'


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fileds = '__all__'

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

class Asked_QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asked_Questions
        fields = '__all__'

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'