# Generated by Django 3.0.6 on 2020-06-11 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200611_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endtrip',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]