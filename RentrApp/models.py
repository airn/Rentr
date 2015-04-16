from django.db import models

# Create your models here.
MAX_SIZE = 100

# products that will app ear in catalog/inventory
class Rentable(models.Model):
    type = models.CharField(max_length=MAX_SIZE,default='Default Product Name')
    isRented = models.BooleanField(default=False)
    dateRented = models.DateTimeField(null=True)
    dateDue = models.DateTimeField(null=True)
    dateReturned = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    store = models.ForeignKey('Store', null=True)

    def __str__(self):
        return self.type

# store information
class Store(models.Model):
    name = models.CharField(max_length=MAX_SIZE,default='Default Store Name')
    address = models.CharField(max_length=MAX_SIZE,default='Default Store Address')
    phoneNum = models.CharField(max_length=MAX_SIZE,default='Default Store Phone Number')

    def __str__(self):
        return self.name
    
# tracks who has rented what
class Rental(models.Model):
    cusName = models.CharField(max_length=MAX_SIZE,default='Default Customer Name')
    cusPhoneNum = models.CharField(max_length=MAX_SIZE,default='Default Customer Phone Number')
    cusEmail = models.CharField(max_length=MAX_SIZE,default='Default Customer Email')
    price = models.FloatField(default=0.00)
    rentable = models.ForeignKey('Rentable', null=True)

    def __str__(self):
        return self.cusName

