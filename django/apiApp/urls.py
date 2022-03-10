from django.urls import re_path
from apiApp import views

from django.conf.urls.static import static #adding url root for api method
from django.conf import settings


urlpatterns=[
    re_path(r'^Company$',views.companyApi),
    re_path(r'^Company/([0-9]+)$',views.companyApi), #Metacharacters are characters that are interpreted in a special way by a RegEx engine. Here's a list of metacharacters:[] . ^ $ * + ? {} () \ | ----> https://www.programiz.com/python-programming/regex

    re_path(r'^JobOffer$',views.jobOfferApi),
    re_path(r'^JobOffer/([0-9]+)$',views.jobOfferApi), 

    re_path(r'^JobOffer/savefile',views.SaveFile)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)