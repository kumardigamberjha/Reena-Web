# Generated by Django 4.1.4 on 2023-01-05 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0005_alter_bookingmodel_payment_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingmodel',
            name='BookingTime',
            field=models.DateTimeField(auto_now_add=True, default='2023-01-01 14:43:43'),
            preserve_default=False,
        ),
    ]
