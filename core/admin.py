from django.contrib import admin
from .models import Car, Cargo, Location



class Show_Id(admin.ModelAdmin):
    list_display=("id",)
# Register your models here.

admin.site.register(Car,Show_Id)
admin.site.register(Cargo,Show_Id)
admin.site.register(Location,Show_Id)