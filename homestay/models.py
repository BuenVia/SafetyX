from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=45, null=True)
    country = models.CharField(max_length=90, null=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=255)
    apartment_number = models.CharField(max_length=10, null=True)
    building_name = models.CharField(max_length=255, null=True)
    street_one = models.CharField(max_length=255)
    street_two = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=45)
    municipality = models.CharField(max_length=255)
    country = models.CharField(max_length=45)
    post_code = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
        return self.name
    
"""
Primary account (user) should be the Business. 
The properties will then be associated with this account.
The primary account can then create secondary accounts which will have access to properties.
"""
