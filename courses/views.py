from rest_framework import generics
from .models import Ourpartners, Community, Course, Lesson, Teacher, Benefits, \
                    Testimonials, AskedQuestions, Resources
from .serializers import OurpartnersSerializer, CommunitySerializer, CourseSerializer, LessonSerializer, TeacherSerializer, \
                    TestimonialsSerializer, BenefitsSerializer, \
                    AskedQuestionsSerializer, ResourcesSerializer

class OurpartnersListCreateView(generics.ListAPIView):
    queryset = Ourpartners.objects.all()
    serializer_class = OurpartnersSerializer


class CommunityListCreateView(generics.ListAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonCreateView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class TeacherListCreateView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class BenefitsListCreateView(generics.ListAPIView):
    queryset = Benefits.objects.all()
    serializer_class = BenefitsSerializer


class TestimonialsListCreateView(generics.ListAPIView):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer


class AskedQuestionsListCreateView(generics.ListAPIView):
    queryset = AskedQuestions.objects.all()
    serializer_class = AskedQuestionsSerializer


class ResourcesListCreateView(generics.ListAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer