# Generated by Django 4.2.6 on 2023-10-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebula_backend', '0002_alter_raider_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raider',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
