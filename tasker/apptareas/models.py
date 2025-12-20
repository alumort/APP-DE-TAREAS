from django.db import models

# Create your models here.
from django.utils import timezone

class Task(models.Model):
    taskname = models.CharField("Task name: ", max_length = 100, blank = False)
    taskdescription = models.CharField("Description and status(finished/todo/in progress)): ", max_length = 400, blank = True)
    createdAt = models.DateTimeField(null = False, blank= True, default = timezone.now())
    lastModified = models.DateTimeField(null = False, blank= True, default = timezone.now())
    
    def __str__(self):
        return self.taskname


