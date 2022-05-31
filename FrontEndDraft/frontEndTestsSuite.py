import unittest 
from webbrowser import get 
from datasource import *
from unittest import TestCase, mock 

class TestDataSource(unittest.TestCase):
    # def __init__(self):
    #     data = DataSource()
       
    def setUp(self):
        self.theConnection = DataSource.connect(self)
        pass
    
    def testStripOutJunk(self):
        "Test to strip out the junk method"
        tupleWithJunk = [('MIXED MELON SPEARS',), ('EGG WHITE OMELETTINI',), ('COCKTAIL ONIONS',), ('CHUNK WHITE ALBACORE TUNA IN WATER',), ('SEASONAL COOKIE PLATTER',), ('CRACKERS',), ('WHITE WINE VINEGAR',)]
        expectedResult = ['MIXED MELON SPEARS', 'EGG WHITE OMELETTINI', 'COCKTAIL ONIONS', 'CHUNK WHITE ALBACORE TUNA IN WATER', 'SEASONAL COOKIE PLATTER', 'CRACKERS', 'WHITE WINE VINEGAR']
        stripedResult = DataSource.stripOutJunk(self, tupleWithJunk)
        self.assertEqual(stripedResult, expectedResult)

    def testGetProductsFirstItemInResult(self):
        "Method to test getProducts method"
        # strippedProducts = 
        with mock.patch('datasource.DataSource.stripProducts') as mockload:
            mockload.return_value = ['GUMMI SANTAS', 'SPICE DROPS', 'JELLY WREATHS', 'JELLY SANTAS & TREES', 'CRUSHED PEPPERMINT TWISTS', 'CHERRY SLICES', 'HOLIDAY GUMMIES', 'HOLIDAY GEMS', 'SMARTIES', 'GUMMY BEARS', 'PSYCHEDELIC JAWBREAKERS']
        theReturnedProducts = DataSource.getProducts(self, "Holiday Candy Corp, Inc.")
        expectedResult = "GUMMI SANTAS"
        firstResult = theReturnedProducts[0]
        self.assertEqual(expectedResult, firstResult)
        # result = self.data.getAllProducts("G. T. Japan, Inc.")
        # firstResult = result[0]
        # expectedResult = "GUMMI SANTAS" 
        # self.assertEqual(compare)

    # def testGetIngredients(self):
    #     "Method to test the getIngredients method"

if __name__== '__main__':
    unittest.main()
    

     