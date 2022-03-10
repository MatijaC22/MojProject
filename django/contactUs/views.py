from django.shortcuts import render

from rest_framework import status
from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ContactUs
from .serializers import ContactUsSerializer
from django.core.mail import send_mail

# Create your views here.
class ContactUs(APIView):
    
    def get(self, request, format=None):
        contact = self.get_objects.all()
        serializer = ContactUsSerializer(contact, many=True)
        return Response(serializer.data)
    

    # ovo je za post u ContactUs a gore je za uzeti nesto iz contactUs
    def post(self, request, format=None):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = request.data
            print(data)
            message='''
            I am {} and I am from {}. My email is {}. My phone number is {}.
            I need {}
            '''.format(data['name'], data['country'], data['email'], data['phone'], data['message'])
            send_mail(data['name'],message, '',['cmatija2@gmail.com'])
            print(message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

        