from rest_framework import serializers
from RentrApp.models import Rentable, Store, Rental

class RentableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rentable
        fields = ('pk', 'store', 'type', 'isRented', 'dateRented', 'dateDue', 'dateReturned')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('pk', 'name', 'address', 'phoneNum')

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ('cusName', 'cusPhoneNum', 'cusEmail', 'price', 'rentable')
