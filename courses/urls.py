from django.urls import path
from .views import CourseSearchView, BannerListView, OurpartnersListView, CommunityListView, CourseListView, \
            CourseDetailView, SubjectListView, ModuleListView, ContentListView, \
            TeacherListView, TestimonialsListView, BenefitsListView, \
            AskedQuestionsListView, ResourcesListView, PurchaseCourseView, PurchasedCoursesView

app_name = 'courses'
    
urlpatterns = [
    path('courses/search/', CourseSearchView.as_view(), name='course-search'),

    path('banner/', BannerListView.as_view(), name='banner-list'),

    path('partner/', OurpartnersListView.as_view(), name='our-partners-list'),

    path('community/', CommunityListView.as_view(), name='community-list'),

    path('courses/', CourseListView.as_view(), name='course-list'),

    path('<int:course_id>/purchase/', PurchaseCourseView.as_view(), name='purchase-course'),

    path('purchased-courses/', PurchasedCoursesView.as_view(), name='purchased-courses'),

    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

    path('subjects/', SubjectListView.as_view(), name='subject-list'),

    path('courses/<int:course_id>/modules/', ModuleListView.as_view(), name='module-list-by-course'),

    path('modules/<int:module_id>/content/', ContentListView.as_view(), name='content-list-by-module'),

    path('teacher/', TeacherListView.as_view(), name='teacher-list'),

    path('benefits/', BenefitsListView.as_view(), name='benefits-list'),

    path('testimonials/', TestimonialsListView.as_view(), name='testimonials-list'),

    path('Asked-Questions/', AskedQuestionsListView.as_view(), name='Asked-Questions-list'),

    path('resources/', ResourcesListView.as_view(), name='resources-list')
]