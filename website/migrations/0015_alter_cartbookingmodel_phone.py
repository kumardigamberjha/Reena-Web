# Generated by Django 4.1.5 on 2023-02-18 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_remove_cartbookingmodel_services_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartbookingmodel',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]