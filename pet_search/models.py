from django.db import models


# Create your models here.
class Pet(models.Model):
    SPECIES_CHOICES = (
        ('dog', 'Dog'),
        ('cat', 'Cat')
    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES)
