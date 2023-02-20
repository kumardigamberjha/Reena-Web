# Generated by Django 4.1.5 on 2023-02-18 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Booking', '0010_remove_bookingmodel_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingmodel',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
