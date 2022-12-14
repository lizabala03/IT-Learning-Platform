# Generated by Django 4.1.2 on 2022-10-23 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_delete_certificate_delete_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('certificate_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=50)),
                ('phn_number', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
                ('time_duration', models.TimeField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.IntegerField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=20)),
                ('phn_number', models.IntegerField()),
                ('profile_img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_id', models.IntegerField(primary_key=True, serialize=False)),
                ('session', models.CharField(max_length=50)),
                ('quiz_mark', models.FloatField(max_length=100)),
                ('course_id', models.ManyToManyField(to='home.course')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('operator', models.CharField(max_length=50)),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('dashboard_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_progress', models.FloatField(max_length=100)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
            ],
        ),
    ]
