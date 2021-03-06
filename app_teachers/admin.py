from django.contrib import admin

from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'qualifications',
        'email',
        'hire_date'
    )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'qualifications')
    list_per_page = 25


# Register your models here.
admin.site.register(Teacher, TeacherAdmin)
