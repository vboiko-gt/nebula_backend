# Generated by Django 4.2.6 on 2023-10-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebula_attendance', '0002_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='points_applied',
            field=models.BooleanField(default=False),
        ),
    ]
