# Generated by Django 2.1.7 on 2019-04-11 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20190403_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_value', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='grade',
        ),
        migrations.AddField(
            model_name='grade',
            name='assignment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.Assignment'),
        ),
    ]
