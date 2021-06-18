from django.db import models

# Create your models here.

class Juego(models.Model):

    AVENTURA = 'aventura'
    FPS = 'fps'
    HORROR = 'horror'
    INFANTIL = 'infantil'
    DEPORTES = 'deportes'

    CATEGORIES_CHOICES = (
        (AVENTURA, 'Aventura'),
        (FPS, 'Fps'),
        (HORROR, 'Horror'),
        (INFANTIL, 'Infatil'),
        (DEPORTES, 'deportes'),
    )

    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)
    precio = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    imagen = models.URLField()

