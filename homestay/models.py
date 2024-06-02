from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
        return self.name
    