# Generated by Django 2.1 on 2022-01-08 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20220108_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='phone_number',
            field=models.CharField(default='+91-', max_length=14),
        ),
    ]
