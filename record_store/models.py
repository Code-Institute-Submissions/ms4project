from django.db import models

from django_mysql.models import ListCharField


class Record(models.Model):
    title = models.CharField(max_length=254)
    artist = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    year = models.IntegerField()
    genre = models.CharField(max_length=25)
    track_listing = ListCharField(
                        base_field=models.CharField(max_length=50),
                        size=50, max_length=(60 * 60))
    description = models.TextField(max_length=500)
    album_art = models.CharField(max_length=254, default="")

    def __str__(self):
        return self.title

