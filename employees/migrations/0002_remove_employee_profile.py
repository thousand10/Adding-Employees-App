# Generated by Django 3.0.6 on 2020-06-01 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='profile',
        ),
    ]