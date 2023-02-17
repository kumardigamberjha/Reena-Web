# Generated by Django 4.1.4 on 2023-01-18 10:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0013_earpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectroPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dermahead1', models.CharField(max_length=100)),
                ('derma1', models.TextField()),
                ('derma2', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
