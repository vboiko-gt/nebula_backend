# Generated by Django 4.2.6 on 2023-10-30 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebula_attendance', '0006_attendee_intime'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='mrt_roster_export',
            field=models.TextField(blank=True),
        ),
    ]
