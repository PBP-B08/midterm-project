# Generated by Django 3.2.15 on 2022-10-28 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0002_area_province'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='province',
            old_name='name',
            new_name='title',
        ),
    ]
