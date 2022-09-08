from statistics import mode
from django.db import models


class people(models.Model):
    name = models.CharField(max_length=225)
    age = models.CharField(max_length=3)
    phone_number = models.CharField(
        max_length=10,
    )
    Aadhar_no = models.CharField(max_length=12)
    salary = models.CharField(max_length=10)
    statement =models.ImageField()
    address = models.CharField(max_length=200)
    rationcard = models.CharField(max_length=8)
    RD_NO = models.CharField(max_length=15, default="RD")
    cardtype = models.CharField(max_length=3)
    District = models.CharField(max_length=25)


class SurveyOfficer(models.Model):
    off_id = models.IntegerField()
    name = models.CharField(max_length=225)
    place = models.CharField(max_length=225)
    no_of_surveys = models.IntegerField()

