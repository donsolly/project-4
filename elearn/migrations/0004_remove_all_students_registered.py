# Generated by Django 3.0.3 on 2020-05-03 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0003_all_students_registered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='all_students',
            name='registered',
        ),
    ]
