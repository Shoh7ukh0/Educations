from django.db import models
from accounts.models import CustomUser
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=100)
    images = models.ImageField(upload_to='courses/Course/img/', blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='courses/Course/video/', blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.title
