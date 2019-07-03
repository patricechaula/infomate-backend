from django.db import models
from users.models import User
from categories.models import Category
# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    pub_date = models.DateField(auto_now=True)
    color = models.IntegerField(default=1)  # 1=red, 2=yellow, 3=green
    summary = models.TextField(max_length=250)
    content = models.TextField()



    def __str__(self):
        return self.title




