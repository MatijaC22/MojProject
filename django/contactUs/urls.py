from django.urls import path

from contactUs import views

urlpatterns = [
    path('contactUs/', views.ContactUs.as_view()),   
]