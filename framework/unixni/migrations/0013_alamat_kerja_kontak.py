# Generated by Django 5.1.2 on 2024-11-18 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unixni', '0012_galeri_galeriutama_galeriitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alamat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Kerja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Kontak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('subtitle', models.CharField(max_length=255)),
                ('description2', models.TextField()),
                ('description3', models.TextField()),
                ('subtitle2', models.CharField(max_length=255)),
            ],
        ),
    ]
