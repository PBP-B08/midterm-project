# Generated by Django 4.1 on 2022-10-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinasi', models.CharField(max_length=50)),
                ('aktivitas', models.CharField(max_length=50)),
                ('lokasi', models.CharField(max_length=50)),
            ],
        ),
    ]
