from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseListCreateView, CourseDetailView, EnrollCourseView, EnrollmentListView, LessonListCreateView, LessonDetailView, CourseMaterialViewSet

router = DefaultRouter()
router.register(r'materials', CourseMaterialViewSet)

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:course_id>/lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('courses/<int:course_id>/lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('courses/<int:course_id>/enroll/', EnrollCourseView.as_view(), name='enroll-course'),
    path('enrollment/', EnrollmentListView.as_view(), name='enrollment-list'),
    path('', include(router.urls)),
]
