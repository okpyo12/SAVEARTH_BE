# Generated by Django 4.1 on 2022-09-15 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0002_remove_route_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='distance',
            field=models.FloatField(),
        ),
    ]