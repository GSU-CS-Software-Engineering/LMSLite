# Generated by Django 2.1.7 on 2019-04-03 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20190403_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='grade',
            field=models.BigIntegerField(blank=True, default=0),
        ),
    ]
