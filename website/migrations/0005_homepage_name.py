# Generated by Django 4.1.4 on 2023-01-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_homepage_home5'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='name',
            field=models.CharField(default='Home', max_length=30),
            preserve_default=False,
        ),
    ]
