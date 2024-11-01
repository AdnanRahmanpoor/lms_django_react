from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer

# Allow authenticated users to create and view courses
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all() 
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(instuctor=self.request.user)

# allow authenticated users to get course details
class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

# allow listing and creating lesson for authenticated users
class LessonListCreateView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return Lesson.objects.filter(course__id=course_id)

    def perform_create(self, serializer):
        course_id =  self.kwargs.get('course_id')
        course = Course.objects.get(id=course_id)
        serializer.save(course=course)

# allow to get, update or delete a lesson for autheticated users
class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

