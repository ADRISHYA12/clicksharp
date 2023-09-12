# Generated by Django 4.2.3 on 2023-08-09 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_contactdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='appoitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('typeofservice', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('remarks', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
