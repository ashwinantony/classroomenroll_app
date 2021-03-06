from django.db import models
from datetime import datetime


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    qualifications = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    # Set 'name' as main field
    def __str__(self):
        return self.name
