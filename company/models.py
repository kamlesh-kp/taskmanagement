from django.db import models


# from django.contrib.auth.models import AbstractUser
#
# class User(AbstractUser):
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

class Employee(models.Model):

    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)

    def __str__(self):
        return self.f_name
