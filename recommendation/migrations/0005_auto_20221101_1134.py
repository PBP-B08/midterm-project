# Generated by Django 3.2.15 on 2022-11-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0004_delete_recommendation'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='image',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='image',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
