from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Banner, Purchase, Ourpartners, Community, Subject, Content, Course, Module, Teacher, Benefits, \
                    Testimonials, AskedQuestions, Resources
from .serializers import BannerSerializer, OurpartnersSerializer, CommunitySerializer, SubjectSerializer, \
                    CourseSerializer, ModuleSerializer, TeacherSerializer, \
                    TestimonialsSerializer, BenefitsSerializer, ContentSerializer, \
                    AskedQuestionsSerializer, ResourcesSerializer, PurchaseSerializer

from rest_framework.permissions import IsAuthenticated
from accounts.serializers import UserProfileSerializer

class PurchasedCoursesView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


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
    

class PurchaseCourseView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        user = request.user

        # Check if the user has already purchased the course
        if Purchase.objects.filter(user=user, course=course).exists():
            return Response({"error": "You have already purchased this course"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new purchase record
        purchase = Purchase.objects.create(user=user, course=course)

        # Add all contents of the purchased course to the user's unlocked contents
        contents_to_unlock = course.contents.all()
        purchase.contents.set(contents_to_unlock)

        serializer = PurchaseSerializer(purchase)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class PurchasedCoursesView(generics.ListAPIView):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        user = self.request.user
        return Purchase.get_purchased_courses(user)


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