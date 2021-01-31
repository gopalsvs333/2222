from django.db import models


# Create your models here.


class Student(models.Model):
    stid=models.IntegerField(primary_key=True)
    roll = models.IntegerField()
    name = models.CharField(max_length=100)
    phone= models.IntegerField()
    add= models.TextField()

class Subject(models.Model):
    marksid =models.IntegerField(primary_key=True)
    maths = models.IntegerField()
    physics= models.IntegerField()
    chemistry=models.IntegerField()
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
