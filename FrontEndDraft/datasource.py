'''Handles all of the data quesries to the SQL database and
provides the apporiatlly formated data to the flask app.
Written by Alice Cutter and Morgan Graves
April-May 2022'''

import psycopg2
import psqlConfig as config

class DataSource:

    def __init__(self):
        self.theConnection = self.connect()

    def connect(self):
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def stripOutJunk(self, rawDataTuples):
        '''Strip out the leading and trailing parantheses and apostrophes
        '''
        strippedDataList = []
        # print(rawDataTuples[0])
        for item in rawDataTuples:
            productString = str(item[0])
            strippedDataList.append(productString)
        return(strippedDataList)

    def queryRequest(self, theQueryString, secondaryArgumentString):
        cursor = self.theConnection.cursor()
        if None != secondaryArgumentString:
            cursor.execute(theQueryString, (secondaryArgumentString,))
        else:
            cursor.execute(theQueryString,)
        return (cursor.fetchall())

    def stripProducts(self, products):
        '''Strip the prodcuts of leading parantheses and apostrophes'''
        return self.stripOutJunk(products)

    def getProducts(self, brand):
        '''Gather the products associated with the given brandName'''
        brandProducts = self.queryRequest("SELECT productName FROM products WHERE brandName=%s", brand)
        print("Printing brand products: ", brandProducts)
        return self.stripProducts(brandProducts)

    def getAllProducts(self):
        '''Gather every product name included in the dataset'''
        allProducts = self.queryRequest("SELECT productName FROM products", None)
        print("Printing all products: ", allProducts)
        return self.stripProducts(allProducts)
    
    def getIngredients(self, theProduct):
        '''Gathers the list of ingredients from the given product'''
        allIngredients = self.queryRequest("SELECT ingredients FROM products WHERE productName=%s", theProduct)
        print("Printing all ingredients: ", allIngredients)
        return allIngredients


if __name__ == '__main__':
    my_source = DataSource()
    my_source.connect()
    my_source.getProducts("G. T. Japan, Inc.")
    # my_source.getAllProducts()
    my_source.getIngredients("CUPCAKES")
