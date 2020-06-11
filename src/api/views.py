from django.shortcuts import render

from rest_framework import viewsets
from .models import StartTrip, EndTrip, Country, City, Passenger, Driver, Car, Trip
from .serializers import StartTripSerializer, EndTripSerializer, CountrySerializer, CitySerializer, PassengerSerializer, DriverSerializer, CarSerializer, TripSerializer
from rest_framework.response import Response


class StartTripViewset(viewsets.ModelViewSet):
    queryset = StartTrip.objects.all()
    serializer_class = StartTripSerializer


class EndTripViewset(viewsets.ModelViewSet):
    queryset = EndTrip.objects.all()
    serializer_class = EndTripSerializer


class CountryViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewset(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class PassengerViewset(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class DriverViewset(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class CarViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class TripViewset(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class TripCountViewset(viewsets.ViewSet):

    def list(self, request):
        queryset = Trip.objects.count()
        reponse = {
            "total_trips": queryset
        }
        print(queryset)
        return Response(reponse)


class TripCityViewset(viewsets.ViewSet):

    def list(self, request):
        cities = []
        queryset = City.objects.all()
        print(queryset)
        for ci in queryset:
            cities.append({"city": ci.name,
                           "trips_count": ci.trips.count()})

        return Response(cities)
