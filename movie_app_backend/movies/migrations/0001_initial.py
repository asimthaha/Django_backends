# Generated by Django 4.1.13 on 2023-11-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('actor', models.CharField(max_length=100)),
                ('actress', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=100)),
                ('camera', models.CharField(max_length=100)),
                ('distributor', models.CharField(max_length=100)),
            ],
        ),
    ]
