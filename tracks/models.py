from django.db import models
from django.db.models import ManyToManyField


class Genres(models.Model):
    genre_name = models.CharField(max_length=200)

    def __str__(self):
        return self.genre_name


class Tracks(models.Model):
    track_title = models.CharField(max_length=200)
    track_rating = models.FloatField(max_length=2)
    track_genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
