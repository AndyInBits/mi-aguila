from django.contrib import admin
from .models import StartTrip, EndTrip, Country, City, Passenger, Driver, Car, Trip


admin.site.register(StartTrip)
admin.site.register(EndTrip)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Passenger)
admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Trip)
