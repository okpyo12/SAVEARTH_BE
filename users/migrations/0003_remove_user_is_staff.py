# Generated by Django 4.1 on 2022-09-01 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_is_staff"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_staff",
        ),
    ]
