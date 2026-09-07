from django.db import models

# Create your models here.

from django.db import models


class Enrollment(models.Model):

    full_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    education = models.CharField(max_length=100)

    course = models.CharField(max_length=100)

    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name
