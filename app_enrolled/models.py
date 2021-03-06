from django.db import models
from datetime import datetime


class Enrolled(models.Model):
    class_id = models.IntegerField()
    class_title = models.CharField(max_length=200)
    user_id = models.IntegerField(blank=True)
    student_name = models.CharField(max_length=200)
    student_email = models.CharField(max_length=100)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.student_email

    class Meta:
        verbose_name = 'Student Enrollment'
        verbose_name_plural = 'Enrollments'
