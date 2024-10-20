# Generated by Django 5.1.1 on 2024-10-19 07:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('ticket_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('trip_id', models.CharField(max_length=10)),
                ('traveler_name', models.CharField(max_length=50)),
                ('traveler_number', models.CharField(max_length=15)),
                ('traveler_email', models.EmailField(max_length=254)),
                ('ticket_cost', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
