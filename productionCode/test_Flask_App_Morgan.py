'''This is a test suite for the what2Eat flask app. It is split
into two classes: integration and unit.
Written by Morgan Graves, April 24, 2022'''

import unittest
from unittest import mock, TestCase
from Morgans_basic_app import *



class TestFlaskAppIntegration(unittest.TestCase):
    def setUp(self):
        app.testing = True 
        self.app = app.test_client()
    
    def test_home(self):
        response = self.app.get('/', follow_redirects = True)
        expectedResult = "You have made it to the homepage for what2Eat, welcome :D.<br><br>" \
        "If you would like to return a list of products based on brand, please complete the URL with:<br>" \
        "/Products/brandName<br>Replace brandName with the brand you wish to query.<br><br>" \
        "Please note: Case matters, as does including spaces. If the brand is more than one word" \
        "replace the<br>spaces with %20 in the URL.<br> I.e., FRESH & EASY --> /Products/FRESH%20&%20EASY"
        self.assertEqual(expectedResult, response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)

    def test_request_nonexistent_route(self):
        response = self.app.get('/68o5785vh/ghhjvhg/hjfvkf', follow_redirects = True)
        expectedResult = "Sorry, wrong format, do this: ...81/Products/brandName"
        self.assertEqual(expectedResult, response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)

    def test_route_to_get_All_Products(self):
        with mock.patch('what2Eat.ProductData.getAllProducts') as fake_data:
            fake_data.return_value = "abcdefg"
            response = self.app.get('/Products/FRESH & EASY', follow_redirects = True)
        outputString = "Here is the list of products for the brand FRESH & EASY <br>abcdefg"
        self.assertEqual(outputString, response.data.decode('utf-8'))

    def test_get_All_Products_Brand_Not_in_Datat(self):
        pass


class TestFlaskAppUnit(unittest.TestCase):
    def setUp(self):
        app.testing = True 
        self.app = app.test_client()

    def test_get_All_Products(self):
        with mock.patch('what2Eat.ProductData.getAllProducts') as fake_data:
            fake_data.return_value = "abcdefg"
            listOfBrandsStatement = get_all_products("Target")
        outputString = f"Here is the list of products for the brand Target <br>abcdefg"
        self.assertEqual(outputString, listOfBrandsStatement)

    def test_brand_Not_Found_Error(self):
        with mock.patch('what2Eat.ProductData.returnBrands') as fake_data:
            fake_data.return_value = ['BrandA', 'BrandB', 'BrandC', 'BrandD']
            resultingString = brand_Not_Found_Error('BrandE')
        expectedString = f"The brand BrandE is not in the database.<br><br>" \
            f"The list of brands in the database are:<br>['BrandA', 'BrandB', 'BrandC', 'BrandD']."
        self.assertEqual(expectedString, resultingString)

if __name__ == '__main__':
    unittest.main()
