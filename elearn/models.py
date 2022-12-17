from django.db import models
from django.contrib.auth.models import User



class Course(models.Model):
   course_short = models.CharField(max_length=50)
   course_full = models.CharField(max_length=50)
   unit = models.CharField(max_length=50)
   level = models.CharField(max_length=50)
   department = models.CharField(max_length=50)
   cost = models.IntegerField()


class Registered_course(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   reg_course_short = models.CharField(max_length=50)
   reg_course_full = models.CharField(max_length=50)
   reg_unit = models.IntegerField()
   cost = models.IntegerField()


class All_students(models.Model):
   matric = models.CharField(max_length=50)
   department = models.CharField(max_length=50)
   level = models.IntegerField()
   paid = models.BooleanField(default=False)


class Broadcast(models.Model):
   level = models.CharField(max_length=50)
   department = models.CharField(max_length=50)
   message = models.CharField(max_length=200)
   title = models.CharField(max_length=50)


class Personal(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   receiver = models.CharField(max_length=50)
   message = models.CharField(max_length=200)
   title = models.CharField(max_length=50)


# Create your models here.
