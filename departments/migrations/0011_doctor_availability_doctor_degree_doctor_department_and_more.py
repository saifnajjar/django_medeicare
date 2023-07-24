# Generated by Django 4.2.3 on 2023-07-22 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0010_remove_doctor_availability_remove_doctor_degree_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='availability',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='degree',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.ForeignKey(default=24, on_delete=django.db.models.deletion.CASCADE, to='departments.department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctors/'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
