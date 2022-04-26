from flask import Flask 
import csv 

import what2Eat 

app = Flask (__name__)

#intializing data 
what2EatObject = what2Eat.ProductData("SmallProductSheet.csv")

def get_all_products (brandName):
    """Function to collect all of the products from the what2EatObject using helper method getAllProducts
    Input: brandName that you are looking for products with.
    Output: text that will be printed to screen as well as all of the products for the given brand. """
    return what2EatObject.getAllProducts(brandName)
  

@app.route('/Products/<brandName>')
def get_products_to_screen(brandName):
    """Function to call get_all_products and return the list of products. 
    Input: brandName and correct routing through URL
    Output: all of the products of a given brandname
    """
    return get_all_products(brandName)
     

@app.errorhandler(404)
def page_not_found(e):
    "Error screen for when the format of the URL is not correct "
    return "Page not found :(. It seems as if the URL you have entered is not correct. To return to the homepage delete everything in the URL after the first \.  "



@app.route('/')
def homepage():
    """Home page for app. Gives user the instructions they need to navigate the application
        Input: Users must not have anything beyond base url in the search bar. 
        Output: Returns a statement helping users figure out how to navigate website"""
        
    
    return 'Welcome to the homepage of What2Eat!. This website returns all of the products of a specified brand <br><br>"\
            "To get a list of products by a given brand enter the following into the search bar after the homepage URL <br><br>"\
            "/Products/[Brand Name] (Please note that the URL is case sensitive so be carefull when you type it in.)'






if __name__ == '__main__':
     app.run()
