# Generated by Django 4.1.5 on 2023-03-06 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_cartbookingmodel_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartbookingmodel',
            name='time',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='website.timings'),
            preserve_default=False,
        ),
    ]
