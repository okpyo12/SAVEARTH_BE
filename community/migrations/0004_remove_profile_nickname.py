# Generated by Django 4.1 on 2022-09-06 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0003_rename_liked_board_like_cnt_profile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="nickname",
        ),
    ]
