from django.db import models
from accounts.models import CustomUser
from django.contrib.auth.models import User

class Our_partners(models.Model):
    images = models.ImageField(upload_to='courses/our_partners/images/', blank=True, null=True)

    def __str__(self):
        return self.images
    
class Community(models.Model):
    video = models.FileField(upload_to='courses/community/video/', blank=True, null=True)

    def __str__(self):
        return self.video

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
    
class Benefits(models.Model):
    number = models.IntegerField(default=0, blank=True, null=True)
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.title
    
class Teacher(models.Model):
    images = models.ImageField(upload_to='courses/teacher/img/', blank=True, null=True)
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    body = models.TextField()
    telegram = models.URLField()
    instagram = models.URLField()
    facebook = models.URLField()
    x = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return self.name
    
class Testimonials(models.Model):
    images = models.ImageField(upload_to='courses/testimonials/img/', blank=True, null=True)
    name = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.name
    
class Asked_Questions(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.title

class Resources(models.Model):
    title = models.CharField(max_length=250)
    link = models.URLField()

    def __str__(self):
        return self.title