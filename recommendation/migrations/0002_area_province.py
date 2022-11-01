# Generated by Django 3.2.15 on 2022-10-28 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('header', models.CharField(max_length=100)),
                ('summary', models.TextField(help_text='Enter a brief summary of the province', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('summary', models.TextField(help_text='Enter a brief description of the area', max_length=1000)),
                ('description', models.TextField(help_text='Enter a brief description of the area', max_length=1000)),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recommendation.province')),
            ],
        ),
    ]