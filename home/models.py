from django.db import models
from django.contrib.auth.models import User

class HomeItems(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    box1 = models.TextField()
    box2 = models.TextField()
    image = models.FileField(upload_to="images/", blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

