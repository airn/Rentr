from rest_framework import serializers
from RentrApp.models import Rentable, Store, Rental

class RentableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rentable
        fields = ('store', 'type', 'isRented', 'dateRented', 'dateDue', 'dateReturned')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Store
        fields = ('pk', 'name', 'address', 'phoneNum')

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rental
        fields = ('cusName', 'cusPhoneNum', 'cusEmail', 'price', 'rentable')
