# Generated by Django 4.1.2 on 2022-12-12 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_remove_contact_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='course_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]
