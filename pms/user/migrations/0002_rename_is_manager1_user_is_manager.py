# Generated by Django 3.2.18 on 2023-03-13 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_manager1',
            new_name='is_manager',
        ),
    ]
