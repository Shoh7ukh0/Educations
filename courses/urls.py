from django.urls import path
from .views import OurpartnersListCreateView, CommunityListCreateView, CourseListCreateView, \
            CourseDetailView, LessonCreateView, \
            TeacherListCreateView, TestimonialsListCreateView, BenefitsListCreateView, \
            AskedQuestionsListCreateView, ResourcesListCreateView

app_name = 'courses'
    
urlpatterns = [
    path('partner/', OurpartnersListCreateView.as_view(), name='our-partners-list-create'),
    path('community/', CommunityListCreateView.as_view(), name='community-list-create'),
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson-create'),
    path('teacher/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('benefits/', BenefitsListCreateView.as_view(), name='benefits-list-create'),
    path('testimonials/', TestimonialsListCreateView.as_view(), name='testimonials-list-create'),
    path('Asked-Questions/', AskedQuestionsListCreateView.as_view(), name='Asked-Questions-list-create'),
    path('resources/', ResourcesListCreateView.as_view(), name='resources-list-create')
]