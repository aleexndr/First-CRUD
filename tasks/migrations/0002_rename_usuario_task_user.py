# Generated by Django 4.2.3 on 2023-07-09 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='usuario',
            new_name='user',
        ),
    ]
