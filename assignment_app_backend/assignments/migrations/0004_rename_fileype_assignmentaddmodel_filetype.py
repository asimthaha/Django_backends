# Generated by Django 4.1.13 on 2023-11-16 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0003_alter_assignmentaddmodel_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignmentaddmodel',
            old_name='fileype',
            new_name='fileType',
        ),
    ]
