# Generated by Django 4.1.2 on 2022-12-13 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0048_alter_course_time_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='time_duration',
        ),
    ]