# Generated by Django 4.2.9 on 2024-03-06 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_customer_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PickupSchedule',
            new_name='PickupScheduleForm',
        ),
    ]
