# Generated by Django 4.2.3 on 2023-07-22 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0009_remove_doctor_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='image',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='name',
        ),
    ]