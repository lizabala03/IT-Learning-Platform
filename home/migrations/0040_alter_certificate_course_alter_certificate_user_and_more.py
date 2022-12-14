# Generated by Django 4.1.2 on 2022-12-13 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_alter_contact_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.course'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='home.user'),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.course'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
    ]
