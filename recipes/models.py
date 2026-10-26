from django.db import models
from django.utils import timezone

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    body = models.TextField()
    published = models.DateTimeField("date published", default=timezone.now())
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
