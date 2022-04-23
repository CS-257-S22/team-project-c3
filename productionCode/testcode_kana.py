"""
    File@ testcode_kana.py
    Author@ Kana Hashimoto
"""
import unittest
from webbrowser import get
from what2Eat import *

class TestIngredient(unittest.TestCase):
    def setUp(self):
        """Set the file used to test functions"""
        self.sampleData = ProductData("SmallProductSheet.csv")
        self.wrongNames = ["Random", " ", "", "1", 1, "$*&@:"]

    def test_load_csv_file(self):
        """Testing if the function load_csv_file returns a nested list"""
        result = self.sampleData.load_csv_file()
        ifNested = any(isinstance(row, list) for row in result)
        self.assertTrue(ifNested)

    def test_returnBrands(self):
        """Testing if returnBrands returns all brands correctly"""
        result = self.sampleData.returnBrands()
        brandList = ['G. T. Japan, Inc.', 'FRESH & EASY', "McConnell's Ice Cream Inc.",
         'Stater Bros. Markets Inc.', 'Meijer, Inc.', 'Target Stores', 
         'Milton G. Waldbaum Company', 'Columbus Manufacturing, Inc.', 
         'DCI Cheese Company, Inc.', 'FRESH&EASY', 'FRESH & TASTY', 
         'FRESH & EASY NEIGHBORHOOD MARKET INC.', 'FRESH & EASY ORGANIC']
        self.assertEqual(result, brandList)

    def test_isValidBrand_True(self):
        """Testing if isValidBrand returns True when getting a correct brand name"""
        result = self.sampleData.isValidBrand("FRESH & EASY")
        self.assertTrue(result)

    def test_isValidBrand_False(self):
        """Testing if isValidBrand returns False when getting a nonexisting brand name"""
        listInvalidInput = ['FRESH OR EASY', 'Fresh & easy', 'fresh & easy', '123', 123, '#*(@&', '', ' ']
        for item in listInvalidInput:
            result =self.sampleData.isValidBrand(item)
            self.assertFalse(result)

    def test_getAllProducts(self):
        """Testing if getAllProducts returns all products when getting a correct brand name"""
        result = self.sampleData.getAllProducts("Stater Bros. Markets Inc.")
        allProducts = ['STATER BROS., SUGAR POWDERED','STATER BROS., PURE CANE SUGAR GRANULATED',
                       'STATER BROS., ROTINI AN ENRICHED MACARONI PRODUCT',
                       'STATER BROS., KIDNEY BEANS, DARK RED']
        self.assertEqual(result, allProducts)

    def test_getProductIngredients(self):
        """Testing if getProductIngredients returns correct ingredients when getting correct product and brand names"""
        result = self.sampleData.getProductIngredients("FRESH & EASY", "BARBECUE SAUCE")
        allIngredients = "tomato puree (water, tomato paste), sugar, distilled vinegar, molasses, water, modified corn starch, salt, bourbon whiskey, contains 1% or less of: mustard flour, spice, dried onion, dried garlic, natural flavor, xanthan gum, caramel color."
        self.assertEqual(result, allIngredients)

    def test_getProductIngredients_falseCombination(self):
        """Testing if getProductIngredients returns None when getting false combination of existing product and brand names"""
        result = self.sampleData.getProductIngredients("Target Stores", "BARBECUE SAUCE")
        self.assertEqual(result, None)

    def test_containIngredients(self):
        """Testing if containIngredients returns True when getting appropriate input"""
        result = self.sampleData.containsIngredient("molasses", "FRESH & EASY", "BARBECUE SAUCE")
        self.assertTrue(result)
    
    def test_containIngredients_FalseIngredients(self):
        """Testing if containIngredients returns alse when getting a wrong ingredient name"""
        result = self.sampleData.containsIngredient("poison", "FRESH & EASY", "BARBECUE SAUCE")
        self.assertFalse(result)
    
    def test_containIngredients_FalseBrand(self):
        """Testing if containIngredients returns alse when getting a wrong brand name"""
        for wrongName in self.wrongNames:
            result = self.sampleData.containsIngredient("molasses", wrongName, "BARBECUE SAUCE")
            self.assertFalse(result)
    
    def test_containIngredients_FalseProduct(self):
        """Testing if containIngredients returns alse when getting a wrong product name"""
        for wrongName in self.wrongNames:
            result = self.sampleData.containsIngredient("molasses", "FRESH & EASY", wrongName)
            self.assertFalse(result)

    def test_brandCarriesProduct_True(self):
        """Testing if brandCarriesProduct True when getting appropriate input"""
        result = self.sampleData.brandCarriesProduct('FRESH & EASY', 'BARBECUE SAUCE')
        self.assertTrue(result)

    def test_brandCarriesProduct_FalseBrand(self):
        """Testing if brandCarriesProduct True when getting a wrong brand name"""
        for wrongName in self.wrongNames:
            result = self.sampleData.brandCarriesProduct(wrongName, 'BARBECUE SAUCE')
            self.assertFalse(result)
    
    def test_brandCarriesProduct_FalseProduct(self):
        """Testing if brandCarriesProduct True when getting a wrong product name"""
        for wrongName in self.wrongNames:
            result = self.sampleData.brandCarriesProduct('FRESH & EASY', wrongName)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

