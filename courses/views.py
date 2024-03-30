from rest_framework import generics
from .models import Course, Lesson, Teacher, Upcoming_Events, \
                    Readers_Opinion, Top_Products, Quick_Links, \
                    Features, Resources
from .serializers import CourseSerializer, LessonSerializer, TeacherSerializer, \
                    Upcoming_EventsSerializer, Readers_OpinionSerializer, \
                    Top_ProductsSerializer, Quick_LinksSerializer, \
                    FeaturesSerializer, ResourcesSerializer

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


class Upcoming_EventsListCreateView(generics.ListAPIView):
    queryset = Upcoming_Events.objects.all()
    serializer_class = Upcoming_EventsSerializer


class Readers_OpinionListCreateView(generics.ListAPIView):
    queryset = Readers_Opinion.objects.all()
    serializer_class = Readers_OpinionSerializer


class Top_ProductsListCreateView(generics.ListAPIView):
    queryset = Top_Products.objects.all()
    serializer_class = Top_ProductsSerializer


class Quick_LinksListCreateView(generics.ListAPIView):
    queryset = Quick_Links.objects.all()
    serializer_class = Quick_LinksSerializer


class FeaturesListCreateView(generics.ListAPIView):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer


class ResourcesListCreateView(generics.ListAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer