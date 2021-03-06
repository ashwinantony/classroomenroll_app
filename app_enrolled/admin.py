from django.contrib import admin

from .models import Enrolled


class EnrolledAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student_name',
        'class_title',
        'student_email',
        'contact_date',
    )
    list_display_links = ('id', 'student_name')
    search_fields = (
        'student_name',
        'class_title',
        'student_email',
    )
    list_per_page = 25


admin.site.register(Enrolled, EnrolledAdmin)
