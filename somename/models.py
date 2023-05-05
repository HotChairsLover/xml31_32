from django.db import models


# Create your models here.
class Pr31(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.title


class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    due_time = models.TimeField()
