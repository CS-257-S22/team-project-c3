from Flask_app.Morgans_basic_app import *
import unittest

class TestFlaskApp(unittest.TestCase):
    def test_home(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects = True)
        expectedResult = "Welcome to the homepage of What2Eat!. This website returns all of the products of a specified brand <br><br>"\
            "To get a list of products by a given brand enter the following into the search bar after the homepage URL <br><br>"\
            "/Products/[Brand Name] (Please note that the URL is case sensitive so be carefull when you type it in.)"
        # expectedResult.encode('utf-8')
        self.assertEqual(expectedResult, response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()