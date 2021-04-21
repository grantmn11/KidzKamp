# Generated by Django 3.1.7 on 2021-04-21 16:48

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_summer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
        migrations.AlterField(
            model_name='summer',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
