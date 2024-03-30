from django.urls import path
from .views import CourseListCreateView, CourseDetailView, LessonCreateView, \
            TeacherListCreateView, Upcoming_EventsListCreateView, \
            Readers_OpinionListCreateView, Top_ProductsListCreateView, \
            Quick_LinksListCreateView, FeaturesListCreateView, ResourcesListCreateView

app_name = 'courses'
    
urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson-create'),
    path('teacher/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('upcoming/', Upcoming_EventsListCreateView.as_view(), name='upcoming-list-create'),
    path('resders/', Readers_OpinionListCreateView.as_view(), name='resders-list-create'),
    path('top_products/', Top_ProductsListCreateView.as_view(), name='top_products-list-create'),
    path('quick_links/', Quick_LinksListCreateView.as_view(), name='quick_links-list-create'),
    path('features/', FeaturesListCreateView.as_view(), name='features-list-create'),
    path('resources/', ResourcesListCreateView.as_view(), name='resources-list-create')
]