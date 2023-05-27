from django.contrib import admin
from django.urls import path, include
from .views import LocationList, CargoList, CarList,get_lat_lng



urlpatterns = [
    path('showcars/', CarList.as_view(), name="car-list"),
    path('showcargoes/', CargoList.as_view(), name="cargo-list"),
    path('showlocations/', LocationList.as_view(), name="location-list"),
    path("showcars/<int:pk>/",CarList.as_view()),
    path("showcargoes/<int:pk>/",CargoList.as_view()),
    path("getlat/",get_lat_lng)
]