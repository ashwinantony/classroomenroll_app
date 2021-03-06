from django.db import models
from datetime import datetime

from app_teachers.models import Teacher


class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    # Set 'title' as main field
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Classroom'
        verbose_name_plural = 'Classrooms'
