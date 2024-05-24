from django.db import models

# Create your models here.

class Technologies(models.Model):
    icon = models.URLField()
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Question(models.Model):
    technology = models.ForeignKey(Technologies, related_name='technologeis', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text