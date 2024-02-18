from django.urls import path
from .views import CourseListCreateView, CourseDetailView, LessonCreateView

app_name = 'courses'
    
urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson-create'),
]