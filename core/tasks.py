from freight.celery import app
from .models import Car, Location
import random


@app.task
def repeat_change_car_location():
    for car in Car.objects.all():
        rand_location=Location.objects.all()
        car.location_place=random.choice(rand_location)
        car.save()