# Generated by Django 4.1.2 on 2022-12-12 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_certificate_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
    ]