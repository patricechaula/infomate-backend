from datetime import timezone

from django.db import models

# Create your models here.

from users.models import User
from categories.models import Category
from datetime import datetime
from django.utils import timezone

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    pub_date = models.DateField(auto_now=True)
    due_date = models.DateField(default=timezone.now())
    notes = models.TextField()
    file_name = models.TextField(default="nofile")
    file_link = models.TextField(default="http://example.com")

    def __str__(self):
        return self.title


