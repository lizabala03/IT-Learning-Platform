# Generated by Django 4.1.2 on 2022-12-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_profile_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='', max_length=20),
        ),
    ]
