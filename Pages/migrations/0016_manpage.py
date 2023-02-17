# Generated by Django 4.1.4 on 2023-01-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0015_alter_electropage_derma1'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dermahead1', models.CharField(max_length=100)),
                ('dermahead2', models.CharField(max_length=100)),
                ('dermahead3', models.CharField(max_length=100)),
                ('dermahead4', models.CharField(max_length=100)),
                ('dermahead5', models.CharField(max_length=100)),
                ('dermahead6', models.CharField(max_length=100)),
                ('derma1', models.TextField()),
                ('derma2', models.TextField()),
                ('derma3', models.TextField()),
                ('derma4', models.TextField()),
                ('derma5', models.TextField()),
                ('derma6', models.TextField()),
                ('derma7', models.TextField()),
            ],
        ),
    ]
