import datetime

from django.db import models


# Create your models here.
class Task(models.Model):
    date = models.DateField(default=datetime.date.today)
    name = models.CharField(max_length=100)
    priority = models.IntegerField()

    def __str__(self):
        return self.name

