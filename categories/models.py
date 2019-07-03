from django.db import models
from users.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField()
    started_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name