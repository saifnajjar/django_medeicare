# Generated by Django 4.2.3 on 2023-08-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='This is a default description.'),
        ),
    ]
