from django.contrib import admin
from . models import Consumers

@admin.register(Consumers)
class ConsumersAdmin(admin.ModelAdmin):
    list_display = ('name', 'EID', 'email')  
    search_fields = ('name', 'EID', 'email', 'driver_license') 
    list_filter = ('drivers_expiry_date', 'vehicle_registration')   
    ordering = ('name',)  

