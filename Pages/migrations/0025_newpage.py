# Generated by Django 4.2.2 on 2023-06-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0024_cacisynergypage_img1_dermalogicapage_img1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
    ]
