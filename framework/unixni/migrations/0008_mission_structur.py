# Generated by Django 5.1.2 on 2024-11-11 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unixni', '0007_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Structur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.TextField()),
            ],
        ),
    ]
