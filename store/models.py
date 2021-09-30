from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 50)


class Seller(models.Model):
    name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=200)
    business_reg_no = models.IntegerField (null=True, blank=True)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=200)
    external_url =models.CharField(null=True, blank=True)

class Customer(models.Model):
    name =models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    phone_number =models.IntegerField()
    password =models