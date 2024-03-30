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
    
class Upcoming_Events(models.Model):
    title = models.CharField(max_length=250)
    link = models.URLField()
    images = models.ImageField(upload_to='courses/Upcoming_Events/img/', blank=True, null=True)
    day = models.DateField()
    date = models.DateField()
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.title
    
class Readers_Opinion(models.Model):
    images = models.ImageField(upload_to='courses/readers_opinion/img/', blank=True, null=True)
    name = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.name
    

class Top_Products(models.Model):
    title = models.CharField(max_length=250)
    link = models.URLField()

    def __str__(self):
        return self.title

class Quick_Links(models.Model):
    title = models.CharField(max_length=250)
    link = models.URLField()

    def __str__(self):
        return self.title

class Features(models.Model):
    title = models.CharField(max_length=250)
    link = models.URLField()

    def __str__(self):
        return self.title

class Resources(models.Model):
    title = models.CharField(max_length=250)
    link = models.URLField()

    def __str__(self):
        return self.title