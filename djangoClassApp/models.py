from django.db import models

# Create your models here.
class Students(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

class Detail(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=10000)

class About(models.Model):
    title = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=10000)

class Services(models.Model):
    topic = models.CharField(max_length=200)
    details = models.CharField(max_length=10000)

class Features(models.Model):
    header = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)

