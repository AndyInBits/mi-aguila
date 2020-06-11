from django.contrib.gis.db import models

# Model of Regions


class StartTrip(models.Model):
    start_date = models.DateTimeField()
    pickup_address = models.CharField(null=False, blank=False, max_length=255)
    pickup_location = models.PointField()

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.', null=True
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.', null=True
    )

    def __str__(self):
        return str(self.start_date)


class EndTrip(models.Model):
    end_date = models.DateTimeField(null=True, blank=True)
    pickup_address = models.CharField(null=False, blank=False, max_length=255)
    pickup_location = models.PointField()

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.', null=True
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.', null=True
    )

    def __str__(self):
        return str(self.end_date)


class Country(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return self.name


class Passenger(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=255)
    last_name = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Driver(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=255)
    last_name = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Car(models.Model):
    plate = models.CharField(null=False, blank=False, max_length=15)

    def __str__(self):
        return self.plate


class Trip(models.Model):
    status = models.CharField(null=False, blank=False,
                              max_length=20, default='OnWay')
    check_code = models.CharField(null=False, blank=False, max_length=10)
    price = models.CharField(null=False, blank=False, max_length=20)
    driver_location = models.PointField(null=True)
    start = models.ForeignKey(StartTrip, on_delete=models.CASCADE)
    end = models.ForeignKey(EndTrip, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, related_name="trips",
                             on_delete=models.CASCADE)
    passanger = models.ForeignKey(
        Passenger, on_delete=models.CASCADE, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.', null=True
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.', null=True
    )

    def __str__(self):
        return "{}-{}-{}".format(self.check_code, self.status, self.city.name)
