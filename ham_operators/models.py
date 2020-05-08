from django.db import models
from django.contrib.auth.models import User
# Create your models here.


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Operator(models.Model):
    call_sign = models.CharField(max_length=10, unique=True)
    licence = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    telephone = models.CharField(max_length=20)
    rig = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.call_sign
