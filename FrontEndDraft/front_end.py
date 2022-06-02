'''Flask app code for the what2Eat website
Written by Morgan Graves and Alice Cutter
April-May 2022'''


from flask import Flask, render_template, request
import csv
from datasource import *

app = Flask(__name__)

#data = []
databaseQuery = DataSource() #initializes new object of datasource 

@app.route('/')
def homepage():
    return render_template('home.html', rows=get_all_products())

def get_ingredients_from_database(theProduct):
    '''
    PARAMETER: theProduct: Producut that the query is searching for
    RETURN: return the results of the query getIngredients
    PURPOSE: Helper function to retrieve ingredients from database
    '''
    
    
    theIngredients = databaseQuery.getIngredients(theProduct)
    return theIngredients

def get_products_from_database(brand):
    '''
    PARAMETER: N/A
    RETURN: Returns the product lists from the query getProducts
    PURPOSE: Helper function to retrieve the prodcuts of the given brand from the database
    '''

    theProducts = databaseQuery.getProducts(brand)
    return theProducts

def get_all_products():
    '''
    PARAMETER: N/A
    RETURN: returns the results of the query getAllProducts
    PURPOSE:Helper funtion to retrieve all of the products in the database
    '''
    allProducts = databaseQuery.getAllProducts()
    return allProducts

@app.route('multiProducts', methods['POST'])
def display_brands_from_identical_products(product);
    '''
    PARAMETER: product: product name that method is looking for identical copies for 
    RETURN: result of query getAllBrandsFromIdenticalProducts (a list of brands where each brand has an item that is same as brand)
    PURPOSE:App route to the multiProducts webpage. This method is intended to pass
    the necessary variables to the template so that it can generate dynamic
    radio buttons
    '''
    
    allBrandsFromIdenticalProducts = databaseQuery.getAllBrandsFromIdenticalProducts(product)
    return render_template('multiProducts', products=get_brand_from_database())

@app.route('/productInfo', methods=['POST'])
def display_product_info_list():
    '''
    PARAMETER: N/A
    RETURN: renders template for individual product page
    PURPOSE:renders the product info page given the product information'
    '''

    ingredients = get_ingredients_from_database(request.form['product']) #need to figure out how you pass the product name that was selected in the autofill bar
    brand = "FRESH & EASY"
    return render_template('productInfo.html', product=get_products_from_database(brand), brand=brand, ingredients=ingredients)

@app.route('/aboutPage')
def display_about_page():
    '''
    PARAMETER: N/A
    RETURN: template for about page
    PURPOSE: Renders template for our about.html page
    '''
    return render_template('about.html', rows=get_all_products()) #need rows so that autofill bar is still available

@app.errorhandler(404)
def page_not_found(e):
    '''
    PARAMETER: N/A
    RETURN: template for 404 page
    PURPOSE: Renders template for our 404.html page
    '''
     return render_template('404.html', rows=get_all_products()) #need rows so that autofill bar is still available

@app.errorhandler(500)
def internal_server_error(e): 
    '''
    PARAMETER: N/A
    RETURN: returns error message 
    PURPOSE: tells coders when there is internal error in program
    '''
    
    
    return "Hmmmm, that didn't seem to work. Use /5111 to return to the homepage and /5111/Products/brandName<br>" \
        "to query the products for the requested brand."

app.run(host='0.0.0.0', port=5111)

    