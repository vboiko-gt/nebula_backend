# Generated by Django 4.2.6 on 2023-10-26 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nebula_backend', '0007_character_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raider',
            name='main',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nebula_backend.character'),
        ),
    ]