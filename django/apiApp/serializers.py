
from rest_framework import serializers
from .models import Company,JobOffer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=('CompanyID','CompanyName')

class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobOffer
        fields=('JobOfferID','JobOfferName','Department','DateOfOffer','LogoPhotoFileName')

    