from rest_framework import serializers
from .models import Car, Cargo, Location
from rest_framework.serializers import ValidationError
from geopy.distance import distance
class IndexLocation(serializers.RelatedField):
    def to_representation(self, value):
        return f"{value.index}"
    def to_internal_value(self, data):
        # index=data.get("index")
        
        try:
            index=Location.objects.get(index=data)
            return index
        except:
            raise ValidationError("this location does not exist")


class CarSerializer(serializers.ModelSerializer):
    location_place=IndexLocation(many=False, queryset=Location.objects.all())
    class Meta:
        model = Car
        fields = ['id', 'number', 'location_place', 'max_weight', ]
        

class CargoSerializer(serializers.ModelSerializer):
    pick_up=IndexLocation(many=False,read_only=True)
    delivery=IndexLocation(many=False,read_only=True)

    class Meta:
        model = Cargo
        fields = ['id', 'pick_up', 'delivery', 'weight', 'description']
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'city', 'state_name', 'index', 'lat', 'lng']
        