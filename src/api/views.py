import json
from rest_framework import viewsets
from django.conf import settings
from django.contrib.gis.geos import Point
from rest_framework.response import Response
from .serializers import StartTripSerializer, EndTripSerializer, CountrySerializer, CitySerializer, PassengerSerializer, DriverSerializer, CarSerializer, TripSerializer
from .models import StartTrip, EndTrip, Country, City, Passenger, Driver, Car, Trip


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


def load_data_json(request):
    import json
    json_path = settings.BASE_DIR + "/trips.json"
    with open(json_path, 'r') as JSON:
        data = json.load(JSON)["trips"]
    for trip in data:
        start = StartTrip.objects.create(
            start_date=trip["start"]["date"]["$date"],
            pickup_address=trip["start"]["pickup_address"],
            pickup_location=Point(float(trip["start"]["pickup_location"]["coordinates"][0]),
                                  float(trip["start"]["pickup_location"]["coordinates"][1])))
        end = EndTrip.objects.create(
            end_date=None,
            pickup_address=trip["end"]["pickup_address"],
            pickup_location=Point(float(trip["end"]["pickup_location"]["coordinates"][0]),
                                  float(trip["end"]["pickup_location"]["coordinates"][1])))
        country, created = Country.objects.get_or_create(
            name=trip["country"]["name"])
        city, created = City.objects.get_or_create(name=trip["city"]["name"])
        if not trip["passenger"]:
            passanger = None
        else:
            passanger, created = Passenger.objects.get_or_create(
                first_name=trip["passenger"]["first_name"], last_name=trip["passenger"]["last_name"])
        if not trip["driver"]:
            driver = None
        else:
            driver, created = Driver.objects.get_or_create(
                first_name=trip["driver"]["first_name"], last_name=trip["driver"]["last_name"])
        if not trip["car"]:
            car = None
        else:
            car, created = Car.objects.get_or_create(
                plate=trip["car"]["plate"])

        if not trip["driver_location"]:
            location = None
        else:
            location = Point(
                trip["driver_location"]["coordinates"][0], trip["driver_location"]["coordinates"][1])

        trip = Trip.objects.create(
            start=start,
            end=end,
            country=country,
            city=city,
            passanger=passanger,
            driver=driver,
            car=car,
            status=trip["status"],
            check_code=trip["check_code"],
            price=trip["price"],
            driver_location=location

        )

    return Response({"status": "ok"}, status=200)
