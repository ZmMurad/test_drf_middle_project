from django.http import Http404
from django.shortcuts import render
from .models import Car, Cargo, Location
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
import random
from geopy.distance import distance
from .serializers import CargoSerializer, CarSerializer, LocationSerializer
from rest_framework import generics,views, response

def new_car():
    rand=f"{random.randint(1000,9999)}{chr(random.randint(65,90))}"
    while Car.objects.filter(number=rand).exists():
        rand=f"{random.randint(1000,9999)}{chr(random.randint(65,90))}"
    rand_location=Location.objects.all()
    
    Car.objects.create(number=rand,max_weight=1000,location_place=random.choice(rand_location))
    



# class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Location.objects.all()
#     serializer_class = Location
    
    
# class CarDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = Car

# class CargoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cargo.objects.all()
#     serializer_class = Cargo
    

class CarList(views.APIView):
    def get(self, request):
        car=Car.objects.all()
        return response.Response(CarSerializer(car,many=True).data)
    def put(self,request,pk, format=None):
        try:
            instance=Car.objects.get(pk=pk)
        except:
            return response.Response({"error":"Object does not exist"})
        
        ser=CarSerializer(instance,data=request.data)
        try:
            ser.is_valid(raise_exception=True)

            # print(Location.objects.get(index=ser.data.get("location_place")))
            # ser.data["location_place"]=
            ser.save()
            return response.Response({"post":ser.data})
        except Exception as e:
            return response.Response({"error":e.args})

    def post(self,request):
        new_car()
        return response.Response({"operation":"succes","new_car_id":Car.objects.last().id})

@api_view(["POST"])
def get_lat_lng(request):
    if request.method=="POST":
        obg=Location.objects.get(index=request.data["index"])
        ser=LocationSerializer(obg)
        
        return response.Response({"data":ser.data})
        
class CargoList(views.APIView):
    def get_object(self, pk):
        try:
            return Cargo.objects.get(pk=pk)
        except Cargo.DoesNotExist:
            raise Http404
    def get(self,request,pk=None):
        if pk:
            obj=self.get_object(pk)
            location_pick_up=Location.objects.get(index=obj.pick_up.index)
            lat_lng_obj=f"{location_pick_up.lat}, {location_pick_up.lng}"
            ser=CargoSerializer(obj)
            cars=[]
            for car in Car.objects.all():
                location_car=Location.objects.get(index=car.location_place.index)
                lat_lng=f"{location_car.lat}, {location_car.lng}"
                cars.append({"number":car.number,"distance":abs(distance(lat_lng,lat_lng_obj).miles)})
            return response.Response({"cargo":ser.data,"cars":cars})
        
        
        cargo=Cargo.objects.all()
        if "weight" in request.data:  
            cargo=Cargo.objects.filter(weight__lte=request.data.get("weight"))
        
        data=CargoSerializer(cargo,many=True).data
        for carg in data:
            miles=450
            location_pick_up=Location.objects.get(index=carg.get("pick_up"))
            lat_lng_obj=f"{location_pick_up.lat}, {location_pick_up.lng}"
            cars=0
            for car in Car.objects.all():
                location_car=Location.objects.get(index=car.location_place.index)
                lat_lng=f"{location_car.lat}, {location_car.lng}"
                if "miles" in request.data:
                    miles=int(request.data.get("miles"))
                if abs(distance(lat_lng,lat_lng_obj).miles)<miles:
                    cars+=1
            carg["near_cars"]=cars
            # data[carg]["near_cars"]=cars
        return response.Response(data)
    def post(self,request):
        ser=CargoSerializer(data=request.data)
        # if not Location.objects.filter(index=request.data.get("pick_up")).exists():
        #     return response.Response({"error":"this location does not exist"})
        try:
            ser.is_valid(raise_exception=True)
                
            ser.save()
        except Exception as e:
            return response.Response({"error":e.args})
        return response.Response(ser.data, status=status.HTTP_201_CREATED)
    def put(self,request,pk):
        obj=self.get_object(pk)
        ser=CargoSerializer(obj,data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return response.Response(ser.data)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return response.Response({"operations":"succesfully deleted"})
        
        


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer