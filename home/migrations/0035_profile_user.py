# Generated by Django 4.1.2 on 2022-12-13 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_remove_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.user'),
        ),
    ]