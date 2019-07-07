from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.title
