# Generated by Django 4.1.4 on 2023-01-03 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingmodel',
            name='datentime',
            field=models.DateTimeField(default='2022-03-01 12:01:01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='name',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='payent_rec',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='pending_paymnet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='services',
            field=models.ManyToManyField(to='Booking.productmodel'),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='total_payment',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
