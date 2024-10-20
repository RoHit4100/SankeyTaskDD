# Generated by Django 5.1.1 on 2024-10-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('user_id', models.CharField(max_length=50)),
                ('route_name', models.CharField(max_length=255)),
                ('route_origin', models.CharField(max_length=255)),
                ('route_destination', models.CharField(max_length=255)),
                ('route_stops', models.JSONField()),
            ],
        ),
    ]
