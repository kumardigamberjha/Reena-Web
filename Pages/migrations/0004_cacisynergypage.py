# Generated by Django 4.1.4 on 2023-01-18 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0003_remove_dermalogicapage_dermahead8'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaciSynergyPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cacihead1', models.CharField(max_length=100)),
                ('cacihead2', models.CharField(max_length=100)),
                ('cacihead3', models.CharField(max_length=100)),
                ('cacihead4', models.CharField(max_length=100)),
                ('cacihead5', models.CharField(max_length=100)),
                ('cacihead6', models.CharField(max_length=100)),
                ('cacihead7', models.CharField(max_length=100)),
                ('cacihead8', models.CharField(max_length=100)),
                ('cacihead9', models.CharField(max_length=100)),
                ('cacihead10', models.CharField(max_length=100)),
                ('cacihead11', models.CharField(max_length=100)),
                ('cacihead12', models.CharField(max_length=100)),
                ('caci1', models.TextField()),
                ('caci2', models.TextField()),
                ('caci3', models.TextField()),
                ('caci4', models.TextField()),
                ('caci5', models.TextField()),
                ('caci6', models.TextField()),
                ('caci7', models.TextField()),
                ('caci8', models.TextField()),
                ('caci9', models.TextField()),
                ('caci10', models.TextField()),
                ('caci11', models.TextField()),
                ('caci12', models.TextField()),
            ],
        ),
    ]
