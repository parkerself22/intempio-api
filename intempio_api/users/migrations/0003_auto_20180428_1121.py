# Generated by Django 2.0.3 on 2018-04-28 15:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_auto_20180428_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='role',
            new_name='name',
        ),
    ]