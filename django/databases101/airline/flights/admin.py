from django.contrib import admin

from flights.models import Airport, Flight, Passenger

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_vertical = ("flight", )

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)