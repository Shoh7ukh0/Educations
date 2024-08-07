from django.db import models
from accounts.models import CustomUser, UserProfile
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .fields import OrderField

class Banner(models.Model):
    images = models.ImageField(upload_to='courses/banners/', blank=True)
        

class Ourpartners(models.Model):
    images = models.ImageField(upload_to='courses/our_partners/images/', blank=True, null=True)

    
class Community(models.Model):
    video = models.FileField(upload_to='courses/community/video/', blank=True, null=True)
    

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)


    class Meta:
        ordering = ['title']
        

    def __str__(self):
        return self.title

class Course(models.Model):
    images = models.ImageField(upload_to='Course/Images')
    students = models.ManyToManyField('accounts.CustomUser', related_name='courses_joined', blank=True)
    owner = models.ForeignKey('accounts.CustomUser', related_name='courses_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    price = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    

class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.title}'
    

class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, 
                                     on_delete=models.CASCADE, 
                                     limit_choices_to={'model__in':('text', 'video', 'image', 'file')}, blank=True, null=True)
    object_id = models.PositiveIntegerField()
    title = models.CharField(max_length=250)
    video = models.FileField(upload_to='Content/Video', blank=True, null=True)
    description = models.TextField(blank=True)
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])
    is_unlocked = models.BooleanField(default=False)


    class Meta:
        ordering = ['order']

    def unlock(self):
        self.is_unlocked = True
        self.save()

class Purchase(models.Model):
    user = models.ForeignKey('accounts.CustomUser', related_name='purchases', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='purchases', on_delete=models.CASCADE)
    modules = models.ManyToManyField(Module, related_name='purchases', blank=True)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} purchased {self.course.title}'

    @classmethod
    def get_purchased_courses(cls, user):
        return cls.objects.filter(user=user).values_list('course__title', flat=True).distinct()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        profile = UserProfile.objects.get_or_create(user=self.user)
        profile.purchased_courses.add(self.course)

    def unlock_modules(self):
        purchased_modules = self.course.modules.all()
        for module in purchased_modules:
            module.unlock()
    
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
    
class AskedQuestions(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.title

class Resources(models.Model):
    title = models.CharField(max_length=250)
    link = models.URLField()

    def __str__(self):
        return self.title