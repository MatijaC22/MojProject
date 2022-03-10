from django.db import models

# Create your models here.


class Company(models.Model):
    CompanyID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=500)

class JobOffer(models.Model):
    JobOfferID = models.AutoField(primary_key=True)
    JobOfferName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfOffer = models.DateField()
    LogoPhotoFileName = models.CharField(max_length=500)