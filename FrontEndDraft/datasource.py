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
        for item in rawDataTuples:
            productString = str(item[0])
            strippedDataList.append(productString)
        return(strippedDataList)


    def stripProducts(self, products):
        '''Strip the prodcuts of leading parantheses and apostrophes'''
        return self.stripOutJunk(products)

    def getProducts(self, brand):
        '''Gather the products associated with the given brandName'''

        cursor = self.theConnection.cursor()
        query = "SELECT productName FROM products WHERE brandName=%s"
        cursor.execute(query, (brand,))
        brandProducts = (cursor.fetchall())
        # return brandProducts
        return self.stripProducts(brandProducts)

    def getAllProducts(self):
        '''Gather every product name included in the dataset'''

        cursor = self.theConnection.cursor()
        query = "SELECT productName FROM products"
        cursor.execute(query,)
        allProducts = (cursor.fetchall())
        # return allProducts
        return self.stripProducts(allProducts)
    
    def getIngredients(self, theProduct):
        '''Gathers the list of ingredients from the given product'''

        cursor = self.theConnection.cursor()
        query = "SELECT ingredients FROM products WHERE productName=%s"
        cursor.execute(query, (theProduct,))
        allProducts = (cursor.fetchall())
        return allProducts



        


if __name__ == '__main__':
    my_source = DataSource()
    my_source.connect()
    # (my_source.getProducts("Holiday Candy Corp, Inc."))
    print(my_source.getProducts("FRESH & EASY"))
    # (my_source.getIngredients("JELLY WREATHS"))git p
