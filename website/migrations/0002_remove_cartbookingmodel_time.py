# Generated by Django 4.1.5 on 2023-03-06 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartbookingmodel',
            name='time',
        ),
    ]
