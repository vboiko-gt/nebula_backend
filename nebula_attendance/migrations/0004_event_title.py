# Generated by Django 4.2.6 on 2023-10-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebula_attendance', '0003_event_points_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]