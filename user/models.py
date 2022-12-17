from django.db import models
from django.contrib.auth.models import User
from elearn.models import *


# Create your models here.
class Profile(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   registered = models.BooleanField(default=False)
   department = models.CharField(max_length=50)
   matric_number = models.CharField(max_length=50)

   def __str__(self):
      return f'{self.user.username} Profile'