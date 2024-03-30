from rest_framework import generics
from .models import Our_partners, Community, Course, Lesson, Teacher, Benefits, \
                    Testimonials, Asked_Questions, Resources
from .serializers import Our_partnersSerializer, CommunitySerializer, CourseSerializer, LessonSerializer, TeacherSerializer, \
                    TestimonialsSerializer, BenefitsSerializer, \
                    Asked_QuestionsSerializer, ResourcesSerializer

class Our_partnersListCreateView(generics.ListCreateAPIView):
    queryset = Our_partners.objects.all()
    serializer_class = Our_partnersSerializer


class CommunityListCreateView(generics.ListCreateAPIView):
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


class Asked_QuestionsListCreateView(generics.ListAPIView):
    queryset = Asked_Questions.objects.all()
    serializer_class = Asked_QuestionsSerializer


class ResourcesListCreateView(generics.ListAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer