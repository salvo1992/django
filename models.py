from django.db import models

class videogame(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    rating=models.IntegerField()

    