# Generated by Django 4.2.6 on 2023-10-30 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebula_attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
