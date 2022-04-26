import unittest 
from webbrowser import get 
from what2Eat import *
#Global Variables
sampleData = ProductData("SmallProductSheet.csv")
testData = sampleData.load_csv_file()


"Testing the functions that are involved in the get products feature. "


class TestLoadCSVFile(unittest.TestCase):
   
    def test1_load_csv_file(self):
        """Testing the function loadCSVFile with the first row of CSV file information written by Alice"""
        testFile = ProductData("SmallProductSheet.csv")
        productData = testFile.load_csv_file()
        firstRow = productData[1]
        testData = ["MOCHI ICE CREAM BONBONS","G. T. Japan, Inc.","ICE CREAM INGREDIENTS: MILK, CREAM, SUGAR, STRAWBERRIES (STRAWBERRIES, SUGAR), CORN SYRUP SOLIDS, SKIM MILK, WHEY, NATURAL FLAVOR, GUAR GUM, MONO & DIGLYCERIDES, BEET JUICE AND BEET POWDER (FOR COLOR), CELLULOSE GUM, LOCUST BEAN GUM, CARRAGEENAN. COATING INGREDIENTS: SUGAR, WATER, RICE FLOUR, TREHALOSE, EGG WHITES, BEET JUICE AND BEET POWDER (FOR COLOR), DUSTED WITH CORN & POTATO STARCH"]

        self.assertEqual(testData, firstRow)

    def test2_load_csv_file(self): 
        """Testing the function loadCSVFile with the last row of CSV file information written by Alice"""
        testFile = ProductData("SmallProductSheet.csv")
        productData = testFile.load_csv_file()
        lastRow = productData[len(productData)-1]
        testData = ["FRESH & EASY, PASTA SAUCE WITH IMPORTED ITALIAN TOMATOES & OLIVE OIL","FRESH & EASY","PLUM TOMATOES, TOMATO PASTE, OLIVE OIL, BLACK OLIVES (BLACK OLIVES, WATER, SALT, FERROUS GLUCONATE), CAPERS (CAPERS, DISTILLED VINEGAR, SALT, WATER), KALAMATA OLIVES (KALAMATA OLIVES, WATER, SALT, RED WINE VINEGAR, EXTRA VIRGIN OLIVE OIL), GARLIC, ANCHOVY PASTE (ANCHOVIES, SALT, OLIVE OIL, ACETIC ACID), PARSLEY, BASIL, ONIONS, WHITE PEPPER, CRUSHED RED PEPPERS, OREGANO."]
        self.assertEqual(testData,lastRow)
    


class TestValidBrandName(unittest.TestCase):
   
    def test_is_Valid_Brand_True(self):
        """Testing the function is_Valid_Brand written by Alice. This test takes in real brand and isValidBrand is expected to
        return true. """
        validBrandBool = sampleData.isValidBrand("G. T. Japan, Inc.")
        self.assertEqual(validBrandBool, True)

    def test_is_Valid_Brand_False(self):
        """Testing the function is_Valid_Brand written by Alice. This test makes
         sure that method returns false when the brand is invalid"""

        invalidBrandBool =  sampleData.isValidBrand("G. T. China, Inc.")
        
        self.assertEqual(invalidBrandBool, False)



if __name__ == '__main__':
    unittest.main()