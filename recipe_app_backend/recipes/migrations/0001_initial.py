# Generated by Django 4.1.13 on 2023-11-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeAddModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('author', models.CharField(default='', max_length=100)),
                ('dateCreated', models.CharField(default='', max_length=100)),
                ('ingredients', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': 'RecipeAddModel',
                'verbose_name_plural': 'RecipeAddModels',
            },
        ),
    ]
