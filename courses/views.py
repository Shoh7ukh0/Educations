from rest_framework import generics
from .models import Ourpartners, Community, Subject, Content, Course, Module, Teacher, Benefits, \
                    Testimonials, AskedQuestions, Resources
from .serializers import OurpartnersSerializer, CommunitySerializer, SubjectSerializer, \
                    CourseSerializer, ModuleSerializer, TeacherSerializer, \
                    TestimonialsSerializer, BenefitsSerializer, ContentSerializer, \
                    AskedQuestionsSerializer, ResourcesSerializer

class OurpartnersListCreateView(generics.ListAPIView):
    queryset = Ourpartners.objects.all()
    serializer_class = OurpartnersSerializer


class CommunityListCreateView(generics.ListAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ModuleListCreateView(generics.ListCreateAPIView):
    serializer_class = ModuleSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        queryset = Module.objects.filter(course_id=course_id)
        return queryset


class ContentListCreateView(generics.ListCreateAPIView):
    serializer_class = ContentSerializer

    def get_queryset(self):
        module_id = self.kwargs.get('module_id')
        queryset = Content.objects.filter(module_id=module_id)
        return queryset


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


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