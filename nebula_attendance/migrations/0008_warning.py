# Generated by Django 4.2.6 on 2023-10-30 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebula_attendance', '0007_event_mrt_roster_export'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('resolved', models.BooleanField(default=False)),
            ],
        ),
    ]
