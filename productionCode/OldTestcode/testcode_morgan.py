from unittest import TestCase, mock
from what2Eat import ProductData

"""Test suite to test the what2Eat method returnBrands
Uses the mock object library https://docs.python.org/3/library/unittest.mock.html
Written by Morgan Graves, April 18th, 2022"""

class TestGetAllProducts(TestCase):

    def test_returnBrands(self):
        """Testing the helper function returnBrands. The test function uses a small 
        sample of data to compare results
        Written by Morgan"""
        testBrandData = [("product_name","brand_name","ingredients"),
                        ('pizza', 'brand 1', 'flour, cheese'),
                        ('cereal', 'brand 2', 'oats, sugar, vitamin B'),
                        ('pot pie', 'brand 3', 'flour, beef, potato, onion')]
        
        with mock.patch('what2Eat.ProductData.load_csv_file') as mockLoad:
            mockLoad.return_value = testBrandData
            brands = ProductData('bogus.csv').returnBrands()

        accurateListOfBrands = ["brand 1","brand 2", "brand 3"]
        for brand in accurateListOfBrands:
            self.assertIn(brand, brands)
        self.assertNotIn("pot pie", brands)

    def test_returnBrandsOnlyBrands(self):
        """Testing that the helper function returnBrands only returns brands. 
        The test function uses a small sample of data to compare results.
        Written by Morgan"""        
        testBrandData = [("product_name","brand_name","ingredients"),
                        ('pizza', 'brand 1', 'flour, cheese'),
                        ('cereal', 'brand 2', 'oats, sugar, vitamin B'),
                        ('pot pie', 'brand 3', 'flour, beef, potato, onion')]
        
        with mock.patch('what2Eat.ProductData.load_csv_file') as mockLoad:
            mockLoad.return_value = testBrandData
            brands = ProductData('bogus.csv').returnBrands()
        self.assertNotIn('pizza', brands)
        self.assertNotIn('brand_name', brands) 

    def test_returnBrandsSingleInstanceOfBrands(self):
        """Testing that the helper function returnBrands only returns one instance of each brand. 
        The test function uses a small sample of data to compare results.
        Written by Morgan"""
        testBrandData = [('pizza', 'brand 1', 'flour, cheese'),
                        ('cereal', 'brand 2', 'oats, sugar, vitamin B'),
                        ('pot pie', 'brand 1', 'flour, beef, potato, onion')]
        
        with mock.patch('what2Eat.what2Eat.load_csv_file') as mockLoad:
            mockLoad.return_value = testBrandData
            brands = ProductData('bogus.csv').returnBrands()

        self.assertEqual(1, brands.count('brand 1'))

    def test_returnBrandsNoEmptyStrings(self):
        """Testing that the helper function returnBrands does not return any empty strings. 
        The test function uses a small sample of data to compare results.
        Written by Morgan"""
        testBrandData = [('pizza', 'brand 1', 'flour, cheese'),
                        ('cereal', '', 'oats, sugar, vitamin B'),
                        ('pot pie', 'brand 3', 'flour, beef, potato, onion')]
        
        with mock.patch('what2Eat.ProductData.load_csv_file') as mockLoad:
            mockLoad.return_value = testBrandData
            brands = ProductData('bogus.csv').returnBrands()
        self.assertNotIn('', brands)
        self.assertEqual(2, len(brands))

    def test_returnBrandsEmptyList(self):
        """Testing that the helper function returnBrands returns an empty list if the passed
        list has no data beyond column lables. The test function uses a small sample of data 
        to compare results.
        Written by Morgan"""
        testBrandData = [("product_name","brand_name","ingredients")]

        with mock.patch('what2Eat.ProductData.load_csv_file') as mockLoad:
            mockLoad.return_value = testBrandData
            brands = ProductData('bogus.csv').returnBrands()
        
        self.assertEqual([], brands)

    def test_returnBrandsEmptyFile(self):
        """Testing that the helper function returnBrands returns an empty list if the file is 
        totally empty. The test function uses a small sample of data to compare results.
        Written by Morgan"""
        testBrandData = []

        with mock.patch('what2Eat.ProductData.load_csv_file') as mockLoad:
            mockLoad.return_value = testBrandData
            brands = ProductData('bogus.csv').returnBrands()
        
        self.assertEqual([], brands)

    def test_returnBrandsFileNotFound(self):
        """Testing that the helper function returnBrands raises a FileNotFoundError if
        the file passed doesn't exist. 
        The test function uses a small sample of data to compare results.
        Written by Morgan"""
        
        with mock.patch("what2Eat.ProductData.load_csv_file") as mockLoad:
            mockLoad.side_effect = FileNotFoundError
            with self.assertRaises(FileNotFoundError):
                brands = ProductData('bogus.csv').returnBrands()
