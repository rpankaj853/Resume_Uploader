# Generated by Django 3.2.3 on 2021-05-31 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newmodel',
            old_name='filemodel',
            new_name='Resume',
        ),
    ]
