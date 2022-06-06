'''Flask app code for the what2Eat website
Written by Morgan Graves and Alice Cutter
April-May 2022'''


from flask import Flask, render_template, request
import csv
from datasource import *

app = Flask(__name__)

data = []
databaseQuery = DataSource()
brand = '' 

global product 
product = ''


@app.route('/')
def homepage():
    '''
    PARAMETER: N/A
    RETURN: template for homepage
    PURPOSE: renders template for the homepage
    '''
    return render_template('home.html', rows=get_all_products())

def get_ingredients_from_database(theProduct, theBrand):
    '''
    PARAMETER: theProduct: Product string that the query is searching for
    RETURN: return the results of the query getIngredients as a list 
    PURPOSE: Helper function to retrieve ingredients from database and return them as a list 
    '''
    theIngredients = databaseQuery.getIngredients(theProduct, theBrand)
    return theIngredients

def get_products_from_database(brand):
    '''
    PARAMETER: brand string  that query is looking for products that belong to it. 
    RETURN: Returns the product lists from the query getProducts
    PURPOSE: Helper function to retrieve the prodcuts of the given brand from the database
    '''
    theProducts = databaseQuery.getProducts(brand)
    return theProducts

def get_all_products():
    '''
    PARAMETER: N/A
    RETURN: returns the list of products from the database query getAllProducts
    PURPOSE:Helper funtion to retrieve all of the products in the database
    '''
    allProducts = databaseQuery.getAllProducts()
    return allProducts


@app.route('/multiProducts', methods=['GET', 'POST'])
def display_brands_from_identical_products():
    '''
    PARAMETER: product: product name (as string) that method is looking for identical copies for 
    RETURN: result of query getAllBrandsFromIdenticalProducts (a list of brands where each brand has an item that is same as brand)
    PURPOSE: App route to the multiProducts webpage. This method is intended to pass
    the necessary variables to the template so that it can generate dynamic
    drop down
    '''
    global product
    if request.method == 'POST':
        myProduct = request.form['product']
        
    elif request.method == 'GET':
        myProduct = request.args['product']
       
    else:
        return "Not a valid request protocol"

    allBrandsFromIdenticalProducts = databaseQuery.getAllBrandsFromIdenticalProducts(myProduct)
    
    if (None == allBrandsFromIdenticalProducts):
        search = request.args['product']

        allBrandsFromSearch = databaseQuery.getSearchBarMatches(search)
        allBrandsFromSearch = allBrandsFromSearch.upper()

        return render_template('multiProducts.html', products = search, brands= allBrandsFromIdenticalProducts, rows=get_all_products())
    else: 
        product = myProduct
        return render_template('multiProducts.html', products=product, brands=allBrandsFromIdenticalProducts, rows=get_all_products())

@app.route('/productInfo', methods=['GET', 'POST'])
def display_product_info_list():
    '''
    PARAMETER: N/A
    RETURN: renders template for individual product page
    PURPOSE:renders the product info page given the product information'
    '''
    if request.method == 'POST':
        brand = request.form['brandChoice']
       
    elif request.method == 'GET':
        brand = request.args['brandChoice']
    else:
        return "Not a valid request protocol"
    ingredients = get_ingredients_from_database(product, brand)
    return render_template('productInfo.html', product=product, brand=brand, ingredients=ingredients, rows=get_all_products())

@app.route('/aboutPage')
def display_about_page():
    '''
    PARAMETER: N/A
    RETURN: template for about page
    PURPOSE: Renders template for our about.html page
    '''
    return render_template('about.html', rows=get_all_products())

@app.errorhandler(404)
def page_not_found(e):
    '''
    PARAMETER: N/A
    RETURN: template for 404 page
    PURPOSE: Renders template for our 404.html page
    '''
    return render_template('404.html', rows=get_all_products())

@app.errorhandler(500)
def internal_server_error(e): 
    '''
    PARAMETER: N/A
    RETURN: returns error message 
    PURPOSE: tells coders when there is internal error in program
    '''
    
    return "Hmmmm, that didn't seem to work. Use /5111 to return to the homepage and /5111/Products/brandName<br>" \
        "to query the products for the requested brand."

@app.errorhandler(400)
def bad_request_error(e):
    '''
    PARAMETER: N/A
    RETURNS: error message
    PURPOSE: to handle bad requests
    '''
    print(e)
    return render_template('400.html', rows=get_all_products())

app.run(host='0.0.0.0', port=5111)

    