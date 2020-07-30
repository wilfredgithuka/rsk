## Database models for the artiles app which will be
## holding writeups from users

from django.db import models
from django.contrib.auth.models import User

class Article (models.Model):

    STATUS = (
        (0, "Draft"),
        (1, "Publish")
        )

    pubdate = models.DateTimeField(auto_now = True)
    status = models.IntegerField(max_length = 1, choices = STATUS)
    lead = models.CharField(max_length = 255, blank=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
