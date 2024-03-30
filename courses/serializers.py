from rest_framework import serializers
from .models import Course, Lesson, Teacher, Upcoming_Events, \
                    Readers_Opinion, Top_Products, Quick_Links, \
                    Features, Resources

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

class Upcoming_EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upcoming_Events
        fields = '__all__'

class Readers_OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readers_Opinion
        fields = '__all__'

class Top_ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Top_Products
        fields = '__all__'

class Quick_LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quick_Links
        fields = '__all__'

class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = '__all__'

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'