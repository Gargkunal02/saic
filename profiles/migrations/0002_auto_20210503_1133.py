# Generated by Django 3.1.7 on 2021-05-03 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='roll_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
