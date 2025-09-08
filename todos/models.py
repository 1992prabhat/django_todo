from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    completed_on = models.DateTimeField(null=True)

    def __str__(self):
        return self.task
