# Generated by Django 3.2.18 on 2023-03-13 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_is_manager_user_is_manager1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_devleopr',
            new_name='is_developer',
        ),
    ]
