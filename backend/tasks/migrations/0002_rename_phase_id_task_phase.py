# Generated by Django 5.1.2 on 2024-11-08 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='phase_id',
            new_name='phase',
        ),
    ]
