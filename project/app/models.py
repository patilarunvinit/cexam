from django.db import models

class data(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    gender = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    birthday = models.DateField(max_length=50)


    objects = models.Manager()