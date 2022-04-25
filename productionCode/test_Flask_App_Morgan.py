from Flask_app.Morgans_basic_app import *
import unittest

class TestFlaskApp(unittest.TestCase):
    def setUp(self): 
        app.config['TESTING'] = True  #seems necessary to end process
        self.app = app.test_client()
    
    def test_home(self):
        response = self.app.get('/', follow_redirects = True)
        expectedResult = "You have made it to the homepage for what2Eat, welcome :D.<br><br>" \
        "If you would like to return a list of products based on brand, please complete the URL with:<br>" \
        "/Products/brandName<br>Replace brandName with the brand you wish to query.<br><br>" \
        "Please note: Case matters, as does including spaces. If the brand is more than one word" \
        "replace the<br>spaces with %20 in the URL.<br> I.e., FRESH & EASY --> /Products/FRESH%20&%20EASY"
        expectedResult.encode('utf-8')
        # self.assertIn("You", response.data.decode('utf-8'))
        self.assertEqual(expectedResult, response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()