# Generated by Django 4.1.5 on 2023-02-18 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0009_alter_bookingmodel_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingmodel',
            name='services',
        ),
    ]
