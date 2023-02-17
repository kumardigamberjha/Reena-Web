# Generated by Django 4.1.4 on 2023-01-18 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_aboutuspage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactuspage',
            name='date',
        ),
        migrations.RemoveField(
            model_name='contactuspage',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contactuspage',
            name='message',
        ),
        migrations.AddField(
            model_name='contactuspage',
            name='about1',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactuspage',
            name='about2',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactuspage',
            name='about3',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactuspage',
            name='about4',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactuspage',
            name='about5',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactuspage',
            name='about6',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactuspage',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
