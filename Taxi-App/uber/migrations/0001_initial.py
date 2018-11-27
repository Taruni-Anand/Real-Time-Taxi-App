# Generated by Django 2.1.3 on 2018-11-27 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorid', models.PositiveIntegerField(default=1)),
                ('pickup_datetime', models.DateTimeField()),
                ('dropoff_datetime', models.DateTimeField()),
                ('rate_code', models.PositiveIntegerField(default=1)),
                ('pickup_longitude', models.FloatField()),
                ('pickup_latitude', models.FloatField()),
                ('dropoff_longitude', models.FloatField()),
                ('dropoff_latitude', models.FloatField()),
                ('passenger_count', models.IntegerField(default=1)),
                ('trip_distance', models.FloatField()),
                ('fare_amount', models.FloatField()),
                ('tip_amount', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('payment_type', models.PositiveIntegerField()),
            ],
        ),
    ]
