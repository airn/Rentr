from django.db import models

# Create your models here.
MAX_SIZE = 100

class Rentable(models.Model):
    type = models.CharField(max_length=MAX_SIZE,default='No Type')
    isRented = models.BooleanField(default=False)
    dateRented = models.DateTimeField(null=True)
    dateDue = models.DateTimeField(null=True)
    dateReturned = models.DateTimeField(null=True)
    image = models.ImageField(null=True)
    price = models.FloatField(default=0.00)
    store = models.ForeignKey('Store', null=True)
    
class Store(models.Model):
    name = models.CharField(max_length=MAX_SIZE,default='Default Store Name')
    address = models.CharField(max_length=MAX_SIZE,default='Default Store Address')
    phoneNum = models.CharField(max_length=MAX_SIZE,default='Default Store Phone Number')

