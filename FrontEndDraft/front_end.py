from flask import Flask, render_template, request
import csv
from datasource import *

app = Flask(__name__)

#data = []
databaseQuery = DataSource() #initializes new object of datasource 

@app.route('/')
def homepage():
    return render_template('index.html', rows=get_all_products())

'''We are temporarily keeping this commented out code for reference'''
# def load_data():
#     with open('SampleData.csv', newline='') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             data.append(row)

# def getRowTitles():
#     row_titles = []
#     for row in data:
#         row_titles.append(row[0])

#     return row_titles

# def getRowByTitle(title):
#      for row in data:
#          if row[0] == title:
#              return row
#      return []

# @app.route('/rowbytitle')
# def display_row_by_title():
#         value = getRowByTitle(request.args['rowchoice'])
#         product = value[0]
#         brand = value[1]
#         ingredients = value[2].split(',')

#         return render_template('productInfo.html', product=product, brand=brand, ingredients=ingredients)

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

@app.route('/productInfo')
def display_product_info_list():
    '''renders the product info page given the product information'''
    ingredients = get_ingredients_from_database(request.args['product']) #need to figure out how you pass the product name that was selected in the autofill bar
    return render_template('productInfo.html', product=product, brand=brand, ingredients=ingredients) #how do you also include the brandname info so the template can display it
    #if we want autofill bar available on this page, do we need to also pass rows=get_all_products?

@app.route('/aboutPage')
def display_about_page():
    return render_template('about.html', rows=get_all_products()) #need rows so that autofill bar is still available

@app.errorhandler(404)
def page_not_found(e):
     return render_template('404.html', rows=get_all_products()) #need rows so that autofill bar is still available

@app.errorhandler(500)
def internal_server_error(e): 
    '''Error screen when an internal server error occures'''
    return "Hmmmm, that didn't seem to work. Use /5111 to return to the homepage and /5111/Products/brandName<br>" \
        "to query the products for the requested brand."

app.run(host='0.0.0.0', port=5111)

    