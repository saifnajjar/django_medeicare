# Generated by Django 4.2.3 on 2023-07-20 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0003_medicine_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='category',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]