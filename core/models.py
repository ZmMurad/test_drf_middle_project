from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Location(models.Model):
    city=models.CharField(max_length=200)
    state_name=models.CharField(max_length=40)
    index=models.CharField(max_length=5)
    lat=models.FloatField()
    lng=models.FloatField()



class Cargo(models.Model):
    pick_up=models.ForeignKey(Location, on_delete=models.SET_NULL, null=True,related_name="locations")
    delivery=models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    weight=models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    description=models.TextField()


class Car(models.Model):
    number=models.CharField(max_length=5, unique=True)
    location_place=models.ForeignKey(Location, on_delete=models.SET_NULL,null=True)
    max_weight=models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    
    

    