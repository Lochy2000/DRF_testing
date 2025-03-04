# Generated by Django 5.1.6 on 2025-03-04 14:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='default_profile_ju9xum.jpg', max_length=255, verbose_name='image'),
        ),
    ]
