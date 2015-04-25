from django.core.urlresolvers import reverse
from django.template.defaultfilters import length
from setuptools.compat import unicode
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here

class RentableListTestCase(APITestCase):

    # Tests creating a rentable with a POST
    def test_create_rentable(self):
        print("********************************************")
        print("Test the creation of a rentable using a POST")
        print("********************************************")
        url = reverse('rentable')
        data = {'store': None,
                'type': unicode('WaveRunner'),
                'isRented': True,
                'dateRented': unicode('2015-03-11T23:29:56.947000Z'),  
                'dateDue': unicode('2015-03-11T23:29:56.947000Z'),     
                'dateReturned': unicode('2015-03-11T23:29:56.947000Z'),}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("Expected Status Code %s" % (status.HTTP_201_CREATED))
        print("Returned Status Code %s" % (response.status_code))
        print(response.data)

    # Negative test for creating a rentable
    def test_create_invalid_rentable(self):
        print("*****************************************************")
        print("Test the creation of an invalid rentable using a POST")
        print("*****************************************************")
        url = reverse('rentable')
        data = {'store': '',
                'type': '',
                'isRented': '',
                'dateRented': '',
                'dateDue': '',
                'dateReturned': '',}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("Expected Status Code %s" % (status.HTTP_400_BAD_REQUEST))
        print("Returned Status Code %s" % (response.status_code))

    # Using a GET returns a list of all objects
    def test_rentable_list(self):
        url = reverse('rentable')
        print("***********************************")
        print("Test using a GET to get all objects")
        print("***********************************")
        for x in range(0, 5):
            data = {'store': None,
                'type': unicode('WaveRunner'),
                'isRented': False,
                'dateRented': unicode('2015-03-11T23:29:56.947000Z'),
                'dateDue': unicode('2015-03-11T23:29:56.947000Z'),
                'dateReturned': unicode('2015-03-11T23:29:56.947000Z'),}
            self.client.post(url, data, format='json')
        getResponse = self.client.get(url, format='json')
        print("Number of returned objects")
        print("Expected 5")
        print("Returned %s" % (len(getResponse.data)))
        self.assertEqual(len(getResponse.data), 5)

    # Using a Get when no rentables are saved returns an empty array
    def test_empty_rentable_list(self):
        url = reverse('rentable')
        print("**********************************************")
        print("Test using a GET to get an empty rentable list")
        print("**********************************************")
        getResponse = self.client.get(url, format='json')
        print("Expected []")
        print("Returned %s" % getResponse.data)

class RentableDetailTestCase(APITestCase):

    def test_get_rentable_detail(self):
        print("***************************************************")
        print("Test using a GET to get a rentable by a specific pk")
        print("***************************************************")
        createUrl = reverse('rentable')
        data = {'store': None,
                'type': unicode('WaveRunner'),
                'isRented': True,
                'dateRented': unicode('2015-03-11T23:29:56.947000Z'),
                'dateDue': unicode('2015-03-11T23:29:56.947000Z'),
                'dateReturned': unicode('2015-03-11T23:29:56.947000Z')}
        postResponse = self.client.post(createUrl, data, format='json')
        url = reverse('rentableDetail', kwargs={'pk': '1'})
        getResponse = self.client.get(url, format='json')
        print("Expected: %s" % postResponse.data)
        print("Returned: %s" % getResponse.data)
        self.assertEqual(getResponse.data, postResponse.data)

    def test_get_invalid_rentable(self):
        print("*******************************************************")
        print("Test using a GET to get a 404 when no rentable is found")
        print("*******************************************************")
        url = reverse('rentableDetail', args='5')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print("Expected Status Code %s" % (status.HTTP_404_NOT_FOUND))
        print("Returned Status Code %s" % (response.status_code))
        
        
    # Tests creating a rentable with a POST
    def test_update_rentable(self):
        print("********************************************")
        print("Test the creation of a rentable using a POST")
        print("********************************************")
        url = reverse('rentable')
        data = {'store': None,
                'type': unicode('WaveRunner'),
                'isRented': True,
                'dateRented': unicode('2015-03-11T23:29:56.947000Z'),  
                'dateDue': unicode('2015-03-11T23:29:56.947000Z'),     
                'dateReturned': unicode('2015-03-11T23:29:56.947000Z'),} 
        response = self.client.post(url, data, format='json')
        # Now edit the data
        url = reverse('rentableDetail', args='1')
        data['isRented'] = False
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Expected Status Code %s" % (status.HTTP_200_OK))
        print("Returned Status Code %s" % (response.status_code))
        print(response.data)

    # Negative test for creating a rentable
    def test_update_invalid_rentable(self):
        print("*****************************************************")
        print("Test the creation of an invalid rentable using a POST")
        print("*****************************************************")
        # Create Rentable
        url = reverse('rentable')
        data = {'store': None,
                'type': unicode('WaveRunner'),
                'isRented': True,
                'dateRented': unicode('2015-03-11T23:29:56.947000Z'),  
                'dateDue': unicode('2015-03-11T23:29:56.947000Z'),     
                'dateReturned': unicode('2015-03-11T23:29:56.947000Z'),} 
        response = self.client.post(url, data, format='json')
        # Edit rentable
        url = reverse('rentableDetail', args="1")
        data = {'store': '',
                'type': '',
                'isRented': '',
                'dateRented': '',
                'dateDue': '',
                'dateReturned': '',}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("Expected Status Code %s" % (status.HTTP_400_BAD_REQUEST))
        print("Returned Status Code %s" % (response.status_code))

class StoreDetailTestCase(APITestCase):
    
    def test_get_store_detail(self):
        print("***************************************************")
        print("Test using a GET to get a store by a specific pk")
        print("***************************************************")
        createUrl = reverse('storeList')
        data = {'name': unicode('Hooters'),
                'address': unicode('123 FunLane'),
                'phoneNum': unicode('850-342-8543')}
        postResponse = self.client.post(createUrl, data, format='json')
        url = reverse('store', args="1")
        getResponse = self.client.get(url, format='json')
        print("Expected: %s" % postResponse.data)
        print("Returned: %s" % getResponse.data)
        self.assertEqual(getResponse.data, postResponse.data)

    def test_get_invalid_store(self):
        print("*******************************************************")
        print("Test using a GET to get a 404 when no store is found")
        print("*******************************************************")
        url = reverse('store', args='5')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print("Expected Status Code %s" % status.HTTP_404_NOT_FOUND)
        print("Returned Status Code %s" % response.status_code)

class StoreListTestCase(APITestCase):

    # Using a GET returns a list of all objects
    def test_store_list(self):
        url = reverse('storeList')
        print("***********************************")
        print("Test using a GET to get all objects")
        print("***********************************")
        for x in range(0, 5):
            data = {'name': unicode('Hooters'),
                    'address': unicode('123 Fun Lane'),
                    'phoneNum': unicode('850-657-9384')}
            self.client.post(url, data, format='json')
        getResponse = self.client.get(url, format='json')
        print("Number of returned objects")
        print("Expected 5")
        print("Returned %s" % (len(getResponse.data)))
        self.assertEqual(len(getResponse.data), 5)

    # Using a Get when no store are saved returns an empty array
    def test_empty_store_list(self):
        url = reverse('storeList')
        print("**********************************************")
        print("Test using a GET to get an empty store list")
        print("**********************************************")
        getResponse = self.client.get(url, format='json')
        print("Expected []")
        print("Returned %s" % getResponse.data)

    # Tests creating a store with a POST
    def test_create_store(self):
        print("********************************************")
        print("Test the creation of a store using a POST")
        print("********************************************")
        url = reverse('storeList')
        data = {'pk': 1,
                'name': unicode('Hooters'),
                'address': unicode('123 Fun Lane'),
                'phoneNum': unicode('850-374-9283')}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("Expected Status Code %s" % (status.HTTP_201_CREATED))
        print("Returned Status Code %s" % (response.status_code))
        self.assertEqual(response.data, data)
        print(response.data)

    # Negative test for creating a store
    def test_create_invalid_store(self):
        print("*****************************************************")
        print("Test the creation of an invalid store using a POST")
        print("*****************************************************")
        url = reverse('storeList')
        data = {'name': '',
                'address': '',
                'phoneNum': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("Expected Status Code %s" % status.HTTP_400_BAD_REQUEST)
        print("Returned Status Code %s" % response.status_code)

class RentalListTestCase(APITestCase):

    # Tests creating a rental with a POST
    def test_create_rental(self):
        print("********************************************")
        print("Test the creation of a rental using a POST")
        print("********************************************")
        createUrl = reverse('rentable')
        data = {'store': None,
                'type': unicode('WaveRunner'),
                'isRented': True,
                'dateRented': unicode('2015-03-11T23:29:56.947000Z'),
                'dateDue': unicode('2015-03-11T23:29:56.947000Z'),
                'dateReturned': unicode('2015-03-11T23:29:56.947000Z')}
        self.client.post(createUrl, data, format='json')
        url = reverse('rentalList')
        data = {'cusName': unicode('Jack Daniels'),
                'cusPhoneNum': unicode('850-342-9485'),
                'cusEmail': unicode('hglejd@htomail.com'),
                'price': 23.54,
                'rentable': 1,
                'dateDue': '2015/04/24 19:37'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("Expected Status Code %s" % status.HTTP_201_CREATED)
        print("Returned Status Code %s" % response.status_code)
        print(response.data)

    # Negative test for creating a rentable
    def test_create_invalid_rental(self):
        print("*****************************************************")
        print("Test the creation of an invalid rental using a POST")
        print("*****************************************************")
        url = reverse('rentalList')
        data = {'cusName': '',
                'cusPhoneNum': '',
                'cusEmail': '',
                'price': '',
                'rentable': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("Expected Status Code %s" % (status.HTTP_400_BAD_REQUEST))
        print("Returned Status Code %s" % (response.status_code))

    # Using a GET returns a list of all objects
    def test_rental_list(self):
        url = reverse('rentalList')
        print("***********************************")
        print("Test using a GET to get all objects")
        print("***********************************")
        createUrl = reverse('rentable')
        for x in range(0, 5):
            data = {'store': None,
                    'type': unicode('WaveRunner'),
                    'isRented': False,
                    'dateRented': unicode('2015-03-11T23:29:56.947000Z'),
                    'dateDue': unicode('2015-03-11T23:29:56.947000Z'),
                    'dateReturned': unicode('2015-03-11T23:29:56.947000Z')}
            self.client.post(createUrl, data, format='json')
        for x in range(1, 6):
            data = {'cusName': unicode('Jack Daniels'),
                'cusPhoneNum': unicode('850-342-9485'),
                'cusEmail': unicode('hglejd@htomail.com'),
                'price': 23.54,
                'rentable': x,
                'dateDue': '2015/04/24 19:37'}
            self.client.post(url, data, format='json')
        getResponse = self.client.get(url, format='json')
        print("Number of returned objects")
        print("Expected 5")
        print("Returned %s" % (len(getResponse.data)))
        self.assertEqual(len(getResponse.data), 5)

    # Using a Get when no rentables are saved returns an empty array
    def test_empty_rental_list(self):
        url = reverse('rentable')
        print("**********************************************")
        print("Test using a GET to get an empty rental list")
        print("**********************************************")
        getResponse = self.client.get(url, format='json')
        print("Expected []")
        print("Returned %s" % getResponse.data)

class RentalDetailTestCase(APITestCase):

    def test_get_rental_detail(self):
        print("***************************************************")
        print("Test using a GET to get a rental by a specific pk")
        print("***************************************************")
        createUrl = reverse('rentalList')
        data = {'cusName': unicode('Jack Daniels'),
                'cusPhoneNum': unicode('850-342-9485'),
                'cusEmail': unicode('hglejd@htomail.com'),
                'price': 23.54,
                'rentable': None}
        postResponse = self.client.post(createUrl, data, format='json')
        url = reverse('rental', args="1")
        getResponse = self.client.get(url, format='json')
        print("Expected: %s" % postResponse.data)
        print("Returned: %s" % getResponse.data)
        self.assertEqual(getResponse.data, postResponse.data)

    def test_get_invalid_rental(self):
        print("*******************************************************")
        print("Test using a GET to get a 404 when no rentable is found")
        print("*******************************************************")
        url = reverse('rental', args='5')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print("Expected Status Code %s" % status.HTTP_404_NOT_FOUND)
        print("Returned Status Code %s" % response.status_code)

    def test_post(self):
        url = reverse('rentalList')
        data = {"rentable":"1",
                "cusName":"Bipol Alam",
                "cusPhoneNum":"8502385476",
                "cusEmail":"bipolalam@gmail.com",
                "price":"4",
                "dateDue":"2015/04/24 19:37"}
        self.client.post(url, data, format='json')



