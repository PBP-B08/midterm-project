# Generated by Django 4.1 on 2022-10-29 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things_to_do', '0004_event_province_food_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='pictures/events'),
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to='pictures/food'),
        ),
    ]
