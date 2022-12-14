# Generated by Django 4.1.2 on 2022-12-13 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='profile_id',
        ),
        migrations.AddField(
            model_name='payment',
            name='profile',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
    ]
