from django.db import models

# Create your models here.
MAX_SIZE = 100

# products that will appear in catalog/inventory
class Rentable(models.Model):
    type = models.CharField(max_length=MAX_SIZE,default='Default Product Name')
    isRented = models.BooleanField(default=False)
    dateRented = models.DateTimeField(null=True)
    dateDue = models.DateTimeField(null=True)
    dateReturned = models.DateTimeField(null=True)
    image = models.ImageField(null=True)
    store = models.ForeignKey('Store', null=True)

# store information
class Store(models.Model):
    name = models.CharField(max_length=MAX_SIZE,default='Default Store Name')
    address = models.CharField(max_length=MAX_SIZE,default='Default Store Address')
    phoneNum = models.CharField(max_length=MAX_SIZE,default='Default Store Phone Number')
    
# tracks who has rented what
class Rental(models.Model):
    custName = models.CharField(max_length=MAX_SIZE,default='Default Customer Name')
    custPhoneNum = models.CharField(max_length=MAX_SIZE,default='Default Customer Phone Number')
    custEmail = models.CharField(max_length=MAX_SIZE,default='Default Customer Email')
    price = models.FloatField(default=0.00)
    rentableID = models.ForeignKey('Rentable', null=True)

