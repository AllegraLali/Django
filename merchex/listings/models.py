from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    
    class Genre(models.TextChoices):
        Hip_Hop = "HH"
        SYNTH_POP = "SP"
        ALTERNATIVE_ROCK = "AR"
        REGGAE = "RG"
        COUNTRY = "CT"
    
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biograpphy = models.fields.CharField(max_length=100)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):
    
    class Type(models.TextChoices):
        RECORDS = "REC"
        CLOTHING = "CLO"
        POSTERS = "POS"
        MISCELLANEOUS = "MIS"
    
    def __str__(self):
        return f'{self.title}'

    title = models.fields.CharField(max_length=100)
    type = models.fields.CharField(choices=Type.choices, max_length=5)
    description = models.fields.CharField(max_length=100)
    sold = models.fields.BooleanField(default=True)
    year = models.fields.IntegerField(null=True, blank=True)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    
