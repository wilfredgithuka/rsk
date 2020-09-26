from django.db import models
from django.contrib.auth.models import User

class Operator(models.Model):
    call = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)

    LICENCE_STATUS = (
        ('full', 'Full Licence'),
        ('noobs', 'Noobs Licence'),
        ('none', 'No Licence'),
        ('wait', 'Awaiting Renewal'),
    )

    licence = models.CharField(
        max_length=30,
        choices=LICENCE_STATUS,
        blank=True,
        default='full',
        help_text='Licence Status',
    )

    MEMBERSHIP_STATUS = (
        ('1', 'Chairman'),
        ('2', 'Vice-Chairman'),
        ('3', 'Secretary'),
        ('4', 'Treasurer'),
        ('5', 'Member'),
        ('6', 'Transmission Equipment'),
    )

    membership = models.CharField(
        max_length=30,
        choices=MEMBERSHIP_STATUS,
        blank=True,
        default='5',
        help_text='Membership Status',
    )

    rig = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.call
