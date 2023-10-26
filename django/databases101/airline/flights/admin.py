from django.contrib import admin

from flights.models import Airport, Flight

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)