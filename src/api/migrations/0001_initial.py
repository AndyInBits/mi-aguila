# Generated by Django 3.0.6 on 2020-06-10 21:52

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EndTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateTimeField()),
                ('pickup_address', models.CharField(max_length=50)),
                ('pickup_location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', null=True, verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', null=True, verbose_name='modified at')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StartTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('pickup_address', models.CharField(max_length=50)),
                ('pickup_location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', null=True, verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', null=True, verbose_name='modified at')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='OnWay', max_length=20)),
                ('check_code', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=20)),
                ('driver_location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Car')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Country')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Driver')),
                ('end', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.EndTrip')),
                ('passanger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Passenger')),
                ('start', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.StartTrip')),
            ],
        ),
    ]