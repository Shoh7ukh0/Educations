from rest_framework import generics
from .models import Banner, Ourpartners, Community, Subject, Content, Course, Module, Teacher, Benefits, \
                    Testimonials, AskedQuestions, Resources
from .serializers import BannerSerializer, OurpartnersSerializer, CommunitySerializer, SubjectSerializer, \
                    CourseSerializer, ModuleSerializer, TeacherSerializer, \
                    TestimonialsSerializer, BenefitsSerializer, ContentSerializer, \
                    AskedQuestionsSerializer, ResourcesSerializer

class CourseSearchView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        subject_id = self.request.query_params.get('subject_id')
        title = self.request.query_params.get('title')

        queryset = Course.objects.all()

        if subject_id:
            queryset = queryset.filter(subject_id=subject_id)

        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset
    

class BannerListView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class OurpartnersListView(generics.ListAPIView):
    queryset = Ourpartners.objects.all()
    serializer_class = OurpartnersSerializer


class CommunityListView(generics.ListAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ModuleListView(generics.ListAPIView):
    serializer_class = ModuleSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        queryset = Module.objects.filter(course_id=course_id)
        return queryset


class ContentListView(generics.ListAPIView):
    serializer_class = ContentSerializer

    def get_queryset(self):
        module_id = self.kwargs.get('module_id')
        queryset = Content.objects.filter(module_id=module_id)
        return queryset


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class BenefitsListView(generics.ListAPIView):
    queryset = Benefits.objects.all()
    serializer_class = BenefitsSerializer


class TestimonialsListView(generics.ListAPIView):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer


class AskedQuestionsListView(generics.ListAPIView):
    queryset = AskedQuestions.objects.all()
    serializer_class = AskedQuestionsSerializer


class ResourcesListView(generics.ListAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer