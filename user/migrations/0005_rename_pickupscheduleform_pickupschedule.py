# Generated by Django 4.2.9 on 2024-03-06 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_pickupschedule_pickupscheduleform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PickupScheduleForm',
            new_name='PickupSchedule',
        ),
    ]