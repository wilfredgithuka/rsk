from django.db import models
from django.contrib.auth.models import User

class Manuals(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/', blank=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    LOAN_STATUS = (
        ('.pdf', 'PDF'),
        ('.doc', 'Ms Word <2017'),
        ('.docx', 'Ms Word >2017'),
        ('.jpeg', 'JPEG Image File'),
    )

    format = models.CharField(
        max_length=6,
        choices=LOAN_STATUS,
        blank=True,
        default='.pdf',
        help_text='Document Type/Format',
    )


    class Meta:
        ordering = ['-created_on']

    ## This makes it possible to appear on the admin page
    def __str__(self):
        return self.title

    @property
    def filesize(self):
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x/1000, 2)
            ext = ' kb'
        elif x < y*1000:
            value = round(x/1000000, 2)
            ext = ' Mb'
        else:
            value = round(x/1000000000, 2)
            ext = ' Gb'
        return str(value)+ext
