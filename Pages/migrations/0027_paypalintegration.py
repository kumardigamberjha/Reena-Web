# Generated by Django 4.1.5 on 2023-07-04 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0026_additemmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayPalIntegration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=150)),
                ('secret_key', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
