# Generated by Django 4.1 on 2022-11-02 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recommendation', '0006_auto_20221101_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Event Name')),
                ('description', models.TextField()),
                ('event_date', models.DateField(verbose_name='Event Date')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendation.province')),
            ],
        ),
    ]
