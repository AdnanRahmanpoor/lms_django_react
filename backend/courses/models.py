"""
Creating Course model and Lesson model with appropriate fields
and importing User model to connect the course to a user (instructor in this instance as foreignKey)
"""

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

# Course Model
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses') # links a course to a User model (in this case a instructor)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# Lesson in each course, model
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons') # link the lesson to a course through foreignkey
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course.title})"

class Enrollment(models.Model):

    from .models import Course

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments') # takes the enrolled student data from User model
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments') # links the course enrolled to the student
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course') # prevent duplicate enrollments

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"
    
# Course Material Model
class CourseMaterial(models.Model):
    # defining the different course material types
    MATERIAL_TYPE = [
        ('video', 'Video'),
        ('pdf', 'PDF Document'),
        ('image', 'Image'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='material') # link course material to a course through foreignkey
    title = models.CharField(max_length=255)
    material_type = models.CharField(max_length=10, choices=MATERIAL_TYPE) # type of material, video,pdf, or an image
    file = models.FileField(upload_to='course_materials/')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # tracks the instructor who uploaded the course material
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.get_material_type_display()}"