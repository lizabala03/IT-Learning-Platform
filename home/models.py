from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    user_password = models.CharField(max_length=50)


class Profile(models.Model):
    profile_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    phn_number = models.IntegerField(null=True)

    profile_img = models.ImageField(default='', upload_to= 'profile',null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)



class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=100)



class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    operator = models.CharField(max_length=50)


class Quiz(models.Model):
    quiz_id = models.IntegerField(primary_key=True)
    course = models.ManyToManyField(Course)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    session = models.CharField(max_length=50)
    quiz_mark = models.FloatField(max_length=100)


class Dashboard(models.Model):
    dashboard_id = models.IntegerField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_progress = models.FloatField(max_length=100)


class Certificate(models.Model):
    certificate_id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)



class Contact(models.Model):
    contact_id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phn_number = models.IntegerField()
    comment = models.TextField()