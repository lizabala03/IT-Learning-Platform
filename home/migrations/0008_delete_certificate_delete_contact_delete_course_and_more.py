# Generated by Django 4.1.2 on 2022-10-23 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_certificate_id_remove_course_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Certificate',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Dashboard',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
    ]
