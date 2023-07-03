# Generated by Django 4.2.2 on 2023-06-09 11:31

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0025_newpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
                ('entry_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pages.newpage')),
            ],
        ),
    ]
