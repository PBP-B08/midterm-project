# Generated by Django 4.1 on 2022-10-29 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things_to_do', '0005_alter_event_image_alter_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.URLField(max_length=255),
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.URLField(max_length=255),
        ),
    ]
