# Generated by Django 2.1 on 2021-12-31 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('age', models.IntegerField()),
                ('Aadhar_no', models.IntegerField(max_length=12)),
                ('salary', models.FloatField()),
                ('rationcard', models.CharField(max_length=8)),
                ('cardtype', models.CharField(max_length=3)),
                ('phone_number', models.CharField(max_length=10, primary_key=True)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
