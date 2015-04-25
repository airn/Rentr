from django.http import Http404
from django.forms import model_to_dict
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render
from RentrApp.models import Rentable, Store, Rental
from RentrApp.serializers import RentableSerializer, StoreSerializer, RentalSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from datetime import datetime

# Create your views here.

# Rentable List
class RentableList(APIView):

    # Returns a list of  rentables
    def get(self, request, format='json'):
        try:
            store = request.query_params['store']
            rentals = Rentable.objects.filter(store=store, isRented=False)
        except MultiValueDictKeyError:
            rentals = Rentable.objects.filter(isRented=False)
        serializer = RentableSerializer(rentals, many=True)
        return Response(serializer.data)

    # Creates a new rentable
    def post(self, request, format='json'):
        serializer = RentableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RentableDetail(APIView):

    def get_object(self, pk, format='json'):
        try:
            return Rentable.objects.get(pk=pk)
        except Rentable.DoesNotExist:
            raise Http404

    # Serializes the rentable and returns the individual rentable
    def get(self, request, pk, format='json'):
        rental = self.get_object(pk)
        serializer = RentableSerializer(rental)
        return Response(serializer.data)

    # Updates the returned rentableObject when POST request
    def post(self, request, pk, format='json'):
        rentable = self.get_object(pk)
        rentable.isRented = False
        rentable.dateReturned = datetime.now()
        serializer = RentableSerializer(rentable, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreDetail(APIView):

    def get_object(self, pk, format='json'):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404

    def get(self, request, pk, format='json'):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data)

def make_rental(request, pk):
    context = {"pk": pk}
    return render(request, "rentr/rentable.html", context)

def return_rental(request, pk):
    context_dict = {}
    rentable = Rentable.objects.get(pk=pk)
    rental = Rental.objects.get(rentable=rentable.pk)
    context_dict['rentable'] = model_to_dict(rentable)
    context_dict['rental'] = model_to_dict(rental)
    print context_dict
    return render(request, "rentr/rental.html", context_dict)

#  Store List
class StoreList(APIView):

    # Returns a list of stores
    def get(self, request, format='json'):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request, format='json'):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RentalList(APIView):

    # Returns a list of rentals
    def get(self, request, format='json'):
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)

    # Creates a new rental
    def post(self, request, format='json'):
        print request.data
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            try:
                rentableId = request.data['rentable']
                rentableDateDue = request.data['dateDue']
                rentable = Rentable.objects.get(pk=rentableId)
                rentable.isRented = True
                rentable.dateDue = rentableDateDue
                rentable.dateRented = datetime.now()
                rentable.save()
                serializer.save()
            except Exception as e:
                print e
                raise Http404
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RentalDetail(APIView):

    def get_object(self, pk, format='json'):
        try:
            return Rental.objects.get(pk=pk)
        except Rental.DoesNotExist:
            raise Http404

    # Serializes the rental and returns the individual rental
    def get(self, request, pk, format='json'):
        rental = self.get_object(pk)
        serializer = RentalSerializer(rental)
        return Response(serializer.data)

    # Updates the rental Object when POST request
    def post(self, request, pk, format='json'):
        rental = self.get_object(pk)
        serializer = RentalSerializer(rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Rented(APIView):

    def get(self, request, format='json'):
        try:
            store = request.query_params['store']
            rentals = Rentable.objects.filter(store=store, isRented=True)
        except MultiValueDictKeyError:
            rentals = Rentable.objects.filter(isRented=True)
        serializer = RentableSerializer(rentals, many=True)
        return Response(serializer.data)

