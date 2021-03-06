# Generated by Django 2.2.7 on 2019-11-15 15:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowingRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showing_room_name', models.CharField(max_length=32, unique=True)),
                ('capacity', models.PositiveIntegerField(default=10, validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
