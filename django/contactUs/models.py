from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created',]
    
    def __str__(self):
        return self.name