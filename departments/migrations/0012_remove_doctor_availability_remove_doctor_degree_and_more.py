# Generated by Django 4.2.3 on 2023-07-22 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0011_doctor_availability_doctor_degree_doctor_department_and_more'),
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
            name='department',
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