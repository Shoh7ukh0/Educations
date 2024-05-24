from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('questions/', views.QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(), name='question-detail'),
]
