from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, Serializer
from rest_framework_gis.serializers import GeoModelSerializer
from .models import StartTrip, EndTrip, Country, City, Passenger, Driver, Car, Trip


class StartTripSerializer(GeoModelSerializer, HyperlinkedModelSerializer):

    class Meta:
        model = StartTrip
        geo_field = "pickup_location"
        fields = ('url', 'id', 'start_date',
                  'pickup_address', 'pickup_location')


class EndTripSerializer(GeoModelSerializer, HyperlinkedModelSerializer):

    class Meta:
        model = EndTrip
        geo_field = "pickup_location"
        fields = ('url', 'id', 'end_date', 'pickup_address', 'pickup_location')


class CountrySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Country
        fields = ('url', 'id', 'name',)


class CitySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = City
        fields = ('url', 'id', 'name',)


class PassengerSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Passenger
        fields = ('url', 'id', 'first_name', 'last_name',)


class DriverSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Driver
        fields = ('url', 'id', 'first_name', 'last_name',)


class CarSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Car
        fields = ('url', 'id', 'plate',)


class TripSerializer(GeoModelSerializer, HyperlinkedModelSerializer):
    start = StartTripSerializer(required=True)
    end = EndTripSerializer(required=True)
    country = CountrySerializer(required=True)
    city = CitySerializer(required=True)
    passanger = PassengerSerializer(required=True)
    driver = DriverSerializer(required=True)
    car = CarSerializer(required=True)

    class Meta:
        model = Trip
        fields = ('url', 'id', 'status', 'check_code',
                  'price', 'driver_location', 'start', 'end', 'country', 'city', 'passanger', 'driver', 'car')

    def create(self, validated_data):
        print(validated_data['status'])
        start_data = validated_data.pop('start')
        start_data = StartTrip.objects.create(**start_data)
        end_data = validated_data.pop('end')
        end_data = EndTrip.objects.create(**end_data)
        country_data = validated_data.pop('country')
        country_data = Country.objects.create(**country_data)
        city_data = validated_data.pop('city')
        city_data = City.objects.create(**city_data)
        passanger_data = validated_data.pop('passanger')
        passanger_data = Passenger.objects.create(**passanger_data)
        driver_data = validated_data.pop('driver')
        driver_data = Driver.objects.create(**driver_data)
        car_data = validated_data.pop('car')
        car_data = Car.objects.create(**car_data)
        trip = Trip.objects.create(status=validated_data['status'], check_code=validated_data['check_code'], price=validated_data['price'], driver_location=validated_data[
                                   'driver_location'], start=start_data, end=end_data, country=country_data, city=city_data, passanger=passanger_data, driver=driver_data, car=car_data)

        return trip

    def update(self, instance, validated_data):
        # Update start date
        start_data = validated_data.pop('start')
        start_update = StartTrip.objects.get(id=instance.start.id)
        start_update.start_date = start_data['start_date']
        start_update.pickup_address = start_data['pickup_address']
        start_update.pickup_location = start_data['pickup_location']
        start_update.save()
        # Update end date
        end_data = validated_data.pop('end')
        end_update = EndTrip.objects.get(id=instance.end.id)
        end_update.end_date = end_data['end_date']
        end_update.pickup_address = end_data['pickup_address']
        end_update.pickup_location = end_data['pickup_location']
        end_update.save()
        # Update country
        country_data = validated_data.pop('country')
        country_update = Country.objects.get(id=instance.country.id)
        country_update.name = country_data['name']
        country_update.save()
        # Update city
        city_data = validated_data.pop('city')
        city_update = City.objects.get(id=instance.city.id)
        city_update.name = city_data['name']
        city_update.save()
        # Update Passanger
        passanger_data = validated_data.pop('passanger')
        passanger_update = Passenger.objects.get(id=instance.passanger.id)
        passanger_update.first_name = passanger_data['first_name']
        passanger_update.last_name = passanger_data['last_name']
        passanger_update.save()
        # Update Driver
        driver_data = validated_data.pop('driver')
        driver_update = Driver.objects.get(id=instance.driver.id)
        driver_update.first_name = driver_data['first_name']
        driver_update.last_name = driver_data['last_name']
        driver_update.save()
        # Update Car
        car_data = validated_data.pop('car')
        car_update = Car.objects.get(id=instance.car.id)
        car_update.plate = car_data['plate']
        car_update.save()
        # Update Trip
        instance.status = validated_data['status']
        instance.check_code = validated_data['check_code']
        instance.price = validated_data['price']
        instance.driver_location = validated_data[
            'driver_location']
        instance.save()
        return instance
