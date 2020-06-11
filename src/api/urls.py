
from django.urls import path, include
from rest_framework import routers
from .views import StartTripViewset, EndTripViewset, CountryViewset, CityViewset, PassengerViewset, DriverViewset, CarViewset, TripViewset, TripCountViewset, TripCityViewset

router = routers.DefaultRouter()
router.register(r'start_trips', StartTripViewset)
router.register(r'end_trips', EndTripViewset)
router.register(r'countries', CountryViewset)
router.register(r'cities', CityViewset)
router.register(r'passangers', PassengerViewset)
router.register(r'drivers', DriverViewset)
router.register(r'cars', CarViewset)
router.register(r'trips', TripViewset)
router.register(r'count_trips', TripCountViewset, basename='count-trips')
router.register(r'city_trips', TripCityViewset,
                basename='count-trips-cities')

urlpatterns = [
    path('v1/', include(router.urls)),
]
