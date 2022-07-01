# Generated by Django 4.0.4 on 2022-05-17 14:03

from django.db import migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_alter_guest_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='zip',
            field=localflavor.us.models.USZipCodeField(blank=True, max_length=10),
        ),
    ]
