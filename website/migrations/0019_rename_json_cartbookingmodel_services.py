# Generated by Django 4.1.5 on 2023-02-21 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_remove_cartbookingmodel_services_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartbookingmodel',
            old_name='json',
            new_name='services',
        ),
    ]
