# Generated by Django 4.1.4 on 2023-01-16 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_homepage_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('about1', models.TextField()),
                ('about2', models.TextField()),
                ('about3', models.TextField()),
                ('about4', models.TextField()),
                ('about5', models.TextField()),
                ('about6', models.TextField()),
            ],
        ),
    ]
