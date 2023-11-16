# Generated by Django 4.1.13 on 2023-11-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentAddModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('subject', models.CharField(default='', max_length=100)),
                ('teacher', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=100)),
                ('filetype', models.CharField(default='', max_length=100)),
                ('lastDate', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
