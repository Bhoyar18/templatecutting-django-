from django.db import models

# Create your models here.
class Student(models.Model):
    Email=models.EmailField()
    Password=models.CharField(max_length=60)
    RepeatPassword=models.CharField(max_length=60)
    
