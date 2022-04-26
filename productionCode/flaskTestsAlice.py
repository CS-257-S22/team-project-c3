from flaskAppAlice import *
from what2Eat import *
import unittest

class TestFlaskApp(unittest.TestCase):
    testObj = ProductData("SmallProductSheet.csv")
    def initalize(self):
        """Create app so as to test the functions"""
        self.app = app.test_client()


    def test_home(self):
        
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects = True)
        homePageMessage = b'Welcome to the homepage of What2Eat!. This website returns all of the products of a specified brand <br><br>"\
            "To get a list of products by a given brand enter the following into the search bar after the homepage URL <br><br>"\
            "/Products/[Brand Name] (Please note that the URL is case sensitive so be carefull when you type it in.)'

        self.assertEqual(response.data, homePageMessage)



    def test_getProducts_Route(self):
        self.app = app.test_client()
        testResponse = self.app.get('/Products/G. T. Japan, Inc.', follow_redirects = True)
        brandName = "Products/G. T. Japan, Inc."
        correctResponse = b"['MOCHI ICE CREAM BONBONS']"
        self.assertEqual(testResponse.data, correctResponse )
        
 
if __name__ == '__main__':
    unittest.main()