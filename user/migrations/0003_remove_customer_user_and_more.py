# Generated by Django 4.2.9 on 2024-03-06 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_pickupschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RenameField(
            model_name='pickupschedule',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='pickupschedule',
            old_name='schedule_date',
            new_name='pickup_date',
        ),
        migrations.RenameField(
            model_name='pickupschedule',
            old_name='schedule_time',
            new_name='pickup_time',
        ),
        migrations.RemoveField(
            model_name='pickupschedule',
            name='is_confirmed',
        ),
        migrations.RemoveField(
            model_name='pickupschedule',
            name='user',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
