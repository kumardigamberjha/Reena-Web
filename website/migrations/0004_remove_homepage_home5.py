# Generated by Django 4.1.4 on 2023-01-16 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_contactuspage_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='home5',
        ),
    ]