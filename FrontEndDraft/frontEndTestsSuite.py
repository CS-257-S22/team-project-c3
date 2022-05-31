import unittest 
from webbrowser import get 
from datasource import *
from unittest import TestCase, mock 

class TestDataSource(unittest.TestCase):
    # def __init__(self):
    #     data = DataSource()
       
    def setUp(self):
        pass
    
    def testStripOutJunk(self):
        "Test to strip out the junk method"
        # myresponse= "GUMMI SANTAS" # this is the first row of the array
        # brand = "Holiday Candy Corp, Inc."
        # response = DataSource.getProducts(self, brand)
        tupleWithJunk = ['s']
        # tupleWithJunk = ("(\'Bogus Product Name\'),", "Bogus Brand Name", "Bogus Ingredients")
        expectedResult = ["Bogus Product Name", "Bogus Brand Name", "Bogus Ingredients"]
        stripedResult = DataSource.stripOutJunk(self, tupleWithJunk)
        self.assertEqual(stripedResult, expectedResult)
        print(response[0])
    
    # def testGetProducts(self):
    #     "Method to test getProducts method"
    #     result = self.data.getAllProducts("G. T. Japan, Inc.")
    #     firstResult = result[0]
    #     expectedResult = "GUMMI SANTAS" 
    #     self.assertEqual(compare)
    # def testGetIngredients(self):
    #     "Method to test the getIngredients method"

if __name__== '__main__':
    unittest.main()
    

     