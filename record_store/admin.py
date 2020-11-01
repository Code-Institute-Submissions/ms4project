from django.contrib import admin
from .models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'artist',
        'country',
        'year',
        'genre',
        'track_listing',
        'description',
        'album_art'
    )


admin.site.register(Record, RecordAdmin)
