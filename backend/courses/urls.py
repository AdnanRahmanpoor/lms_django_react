from django.urls import path
from .views import CourseListCreateView, CourseDetailView, LessonListCreateView, LessonDetailView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:course_id>/lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('courses/<int:course_id>/lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
]
