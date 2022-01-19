from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField()
    task = models.CharField(max_length=200)

    def __str__(self):
        return str(self.task)

# class TodoItem(models.Model):
#     content = models.TextField()
#     currentUser = models.ForeignKey(User, on_delete=models.CASCADE)

   