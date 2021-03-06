from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    # To display multiple fields on listing admin page as Table view
    list_display = (
        'id',
        'title',
        'teacher'
    )

    # To make 'id' and 'title' Clickable on the above list.
    # By default only first given field is clickable
    list_display_links = ('id', 'title')

    # To filter list by 'teacher' field
    list_filter = ('teacher',)

    # Search bar for searching in given fields
    search_fields = (
        'title',
        'description',
        'teacher',
    )

    list_per_page = 25


# Register your models here.
admin.site.register(Listing, ListingAdmin)
