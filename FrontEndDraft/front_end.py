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
    '''Helper function to retrieve ingredients from database'''
    theIngredients = databaseQuery.getIngredients(theProduct)
    return theIngredients

def get_products_from_database(brand):
    '''Helper function to retrieve the prodcuts of the given brand from the database'''
    theProducts = databaseQuery.getProducts(brand)
    return theProducts

def get_all_products():
    '''Helper funtion to retrieve all of the products in the database'''
    allProducts = databaseQuery.getAllProducts()
    return allProducts

@app.route('/multiProducts', methods=['POST'])
def display_brands_from_identical_products(product):
    '''App route to the multiProducts webpage. This method is intended to pass
    the necessary variables to the template so that it can generate dynamic
    radio buttons.'''
    allBrandsFromIdenticalProducts = databaseQuery.getAllBrandsFromIdenticalProducts(request.form['product'])
    return render_template('multiProducts.html', products=get_brand_from_database(), brands=allBrandsFromIdenticalProducts)

@app.route('/productInfo', methods=['POST'])
def display_product_info_list():
    '''renders the product info page given the product information'''
    ingredients = get_ingredients_from_database(request.form['product'])
    brand = "FRESH & EASY"
    return render_template('productInfo.html', product=get_products_from_database(brand), brand=brand, ingredients=ingredients)

@app.route('/aboutPage')
def display_about_page():
    return render_template('about.html', rows=get_all_products())

@app.errorhandler(404)
def page_not_found(e):
     return render_template('404.html', rows=get_all_products())

@app.errorhandler(500)
def internal_server_error(e): 
    '''Error screen when an internal server error occures'''
    return "Hmmmm, that didn't seem to work. Use /5111 to return to the homepage and /5111/Products/brandName<br>" \
        "to query the products for the requested brand."

app.run(host='0.0.0.0', port=5111)

    