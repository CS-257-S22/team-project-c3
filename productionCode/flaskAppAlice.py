from flask import Flask 
import csv 
import sys 
import what2Eat 

#need to import from what2EatModule
app = Flask (__name__)

#intialize data 
what2EatObject = what2Eat.ProductData("SmallProductSheet.csv")

def get_all_products (brandName):
    return f"This is the list of all products for the entered brand:{brandName}<br>{what2EatObject.getAllProducts(brandName)}"


@app.route('/Products/<brandName>')
def get_products_to_screen(brandName):
     return get_all_products(brandName)


@app.errorhandler(404)
def page_not_found(e):
    "Error screen for when the format of the URL is not correct "
    return "Page not found :(. It seems as if the URL you have entered is not correct. To return to the homepage delete everything in the URL after the first \.  "
@app.route('/')
def homepage():
    "Homepage for App. Gives user the instructions they need to navigate the application"
    
    return "Welcome to the homepage of What2Eat!. This website returns all of the products of a specified brand <br><br>"\
            "To get a list of products by a given brand enter the following into the search bar after the homepage URL <br><br>"\
            "/Products/[Brand Name] (Please note that the URL is case sensitive so be carefull when you type it in.)"



if __name__ == '__main__':
     app.run()
