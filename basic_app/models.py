from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    principal = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name + ' '+ str(self.pk)

    def get_absolute_url(self):
        return reverse('basic_app:detailScuola',kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def get_absolute_url(self):
        pkSchool = self.school.pk
        return reverse('basic_app:detailScuola',args=(pkSchool,) )

    def __str__(self):
        return self.name
