# Generated by Django 4.1.4 on 2023-01-18 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_dermalogicapage_remove_contactuspage_about1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dermalogicapage',
            name='derma7',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dermalogicapage',
            name='derma8',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]