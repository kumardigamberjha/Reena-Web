# Generated by Django 4.1.4 on 2023-01-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0017_remove_manpage_derma7'),
    ]

    operations = [
        migrations.CreateModel(
            name='MassagePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dermahead1', models.CharField(max_length=100)),
                ('dermahead2', models.CharField(max_length=100)),
                ('dermahead3', models.CharField(max_length=100)),
                ('dermahead4', models.CharField(max_length=100)),
                ('derma1', models.TextField()),
                ('derma2', models.TextField()),
                ('derma3', models.TextField()),
                ('derma4', models.TextField()),
                ('derma5', models.TextField()),
            ],
        ),
    ]
