from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_pic = models.CharField(max_length=40, default="img_avatar.png")
    bio = models.TextField(default="No bio")
    course = models.CharField(max_length=180, default="N/A")
    occupation = models.CharField(max_length=180, default="N/A")
    year = models.IntegerField(default=0)
    reg_no = models.CharField(max_length=10, default="N/A")



