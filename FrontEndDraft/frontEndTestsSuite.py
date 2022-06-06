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
        '''Test to strip out the junk method'''
        tupleWithJunk = [('MIXED MELON SPEARS',), ('EGG WHITE OMELETTINI',), ('COCKTAIL ONIONS',), ('CHUNK WHITE ALBACORE TUNA IN WATER',), ('SEASONAL COOKIE PLATTER',), ('CRACKERS',), ('WHITE WINE VINEGAR',)]
        expectedResult = ['MIXED MELON SPEARS', 'EGG WHITE OMELETTINI', 'COCKTAIL ONIONS', 'CHUNK WHITE ALBACORE TUNA IN WATER', 'SEASONAL COOKIE PLATTER', 'CRACKERS', 'WHITE WINE VINEGAR']
        stripedResult = DataSource().stripOutJunk(tupleWithJunk)
        self.assertEqual(stripedResult, expectedResult)

    def testGetProductsFirstItemInResult(self):
        '''Method to test getProducts method'''
        # strippedProducts = 
        with mock.patch('datasource.DataSource.stripProducts') as mockload:
            mockload.return_value = ['GUMMI SANTAS', 'SPICE DROPS', 'JELLY WREATHS', 'JELLY SANTAS & TREES', 'CRUSHED PEPPERMINT TWISTS', 'CHERRY SLICES', 'HOLIDAY GUMMIES', 'HOLIDAY GEMS', 'SMARTIES', 'GUMMY BEARS', 'PSYCHEDELIC JAWBREAKERS']
        theReturnedProducts = DataSource().getProducts("Holiday Candy Corp, Inc.")
        expectedResult = "GUMMI SANTAS"
        firstResult = theReturnedProducts[0]
        
        self.assertEqual(expectedResult, firstResult)
        

    def testGetProductsLastItemInResult(self):
        '''Tests if all of the products of the given brand are returned.'''
        with mock.patch('datasource.DataSource.stripProducts') as mockload:
            mockload.return_value = ['GUMMI SANTAS', 'SPICE DROPS', 'JELLY WREATHS', 'JELLY SANTAS & TREES', 'CRUSHED PEPPERMINT TWISTS', 'CHERRY SLICES', 'HOLIDAY GUMMIES', 'HOLIDAY GEMS', 'SMARTIES', 'GUMMY BEARS', 'PSYCHEDELIC JAWBREAKERS']
        theReturnedProducts = DataSource().getProducts("Holiday Candy Corp, Inc.")
        expectedResult = "PSYCHEDELIC JAWBREAKERS"
        lastResult = theReturnedProducts[-1]
        self.assertEqual(expectedResult, lastResult)
    
    def testGetIngredients(self):
        '''Test to determine whether getIngredients works'''
        theReturnedIngredients = DataSource().getIngredients('PIGS LIPS', 'BIG JOHNS')
        expectedResult = [('COOKED CURED PIGS LIPS, WATER, SALT, SODIUM ERYTHORBATE, SODIUM NITRITE.',)]
        # print(theReturnedIngredients) 
        self.assertEqual(expectedResult, theReturnedIngredients)

    def testAllBrandsFromIdenticalProducts(self):
        '''Test to determine if getAllBrandsFromIdenticalProducts works'''
        theReturnedBrands = DataSource().getAllBrandsFromIdenticalProducts('CEREAL BARS')
        expectedResult = [('The Kellogg Company'), ('The Kellogg Company'), ('Target Stores'), ('The Kellogg Company'), ('The Kellogg Company'), ('The Kellogg Company'), ('The Kellogg Company'), ('The Kellogg Company'), ('The Kellogg Company'), ('The Kellogg Company'), ('The Kellogg Company'), ('Harris-Teeter Inc.'), ('Ahold Usa, Inc.'), ('Harris-Teeter Inc.'), ('Harris-Teeter Inc.')]
        # print("Printing the returned brands: ", theReturnedBrands)
        self.assertEqual(expectedResult, theReturnedBrands)

    def testGetProductByIDNumber(self):
        '''Tests if a prodcut can be retrieved based on its ID number'''
        theReturnedProduct = DataSource().getProductByIdNumber("45288988")
        expectedResult = [('HOT AND SWEET SLICED GREEN JALAPENOS',)]
        # print("Printing the retuned product based on ID number: ", theReturnedProduct)
        self.assertEqual(expectedResult, theReturnedProduct)

if __name__== '__main__':
    unittest.main()
    

     