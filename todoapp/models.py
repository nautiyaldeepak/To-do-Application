from django.db import models
from datetime import datetime, timedelta

class todoList(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    SubTasks = models.TextField()
    Status = models.TextField()
    DueDate = models.DateField()
    Alert = models.IntegerField()
    Symbol = models.TextField()
    Visibility = models.TextField()
    HardDeleteDate = models.DateField(null=True)
    Local_id = models.CharField(max_length=60)

    def is_in_title(self):
        return str(self.Title)
