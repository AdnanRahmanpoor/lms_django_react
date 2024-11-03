from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Course, Lesson, Enrollment, CourseMaterial
from .serializers import CourseSerializer, LessonSerializer, EnrollmentSerializer, CourseMaterialSerializer

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

# allow authenticated to enroll in course
class EnrollCourseView(generics.CreateAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        course_id = self.kwargs.get('course-id')
        course = Course.objects.get(id=course_id)
        serializer.save(student=self.request.user, course=course)

# list all courses the user is enrolled in
class EnrollmentListView(generics.ListAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user)
    
# coursematerial view for CRUD operations
class CourseMaterialViewSet(viewsets.ModelViewSet):
    serializer_class = CourseMaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CourseMaterial.objects.filter(course__enrolled_students=self.request.user)

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)