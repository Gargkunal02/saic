# Generated by Django 3.2.2 on 2021-05-10 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20210508_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='mobile',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='roll_number',
            field=models.TextField(blank=True, null=True),
        ),
    ]