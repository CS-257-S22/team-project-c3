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
        '''
        PARAMETER:      rawDataTuples: List of the products stored as a teuples with the product in the first index and nothing in the second one. 
        RETURN:     A list of strings where each item is stripped of uncessary characters like quotation marks
        PURPOSE:    Strip out the leading and trailing parantheses and apostrophes
        '''
        strippedDataList = []
        for item in rawDataTuples:
            productString = str(item[0])
            strippedDataList.append(productString)
        return(strippedDataList)

        '''
        INPUT:       
        PARAMETER:     
        PURPOSE:    
        '''

    def queryRequest(self, theQueryString, secondaryArgumentString):
         '''
        PARAMETER: theQueryString: string of the query that will be executed
        PARAMETER: the secondary parameter for the query. Not all queries use it. 
        RETURN:    Returned value of query 
        PURPOSE:    
        '''
        '''Facilitate the query request to the database. Can be utilized w/ or w/out a 
        secondary argument. Returns the fetched data.'''
        cursor = self.theConnection.cursor()
        if None != secondaryArgumentString:
            cursor.execute(theQueryString, (secondaryArgumentString,))
        else:
            cursor.execute(theQueryString,)
        return (cursor.fetchall())

    # def stripProducts(self, products):
    #     '''Strip the prodcuts of leading parantheses and apostrophes'''
    #     return self.stripOutJunk(products)

    def getProducts(self, brand):
        '''Gather the products associated with the given brandName'''
        brandProducts = self.queryRequest("SELECT productName FROM products WHERE brandName=%s", brand)
        #print("Printing brand products: ", brandProducts)
        return self.stripOutJunk(brandProducts)

    def getAllProducts(self):
        '''Gather every product name included in the dataset'''
        allProducts = self.queryRequest("SELECT productName FROM products", None)
        #print("Printing all products: ", allProducts)
        return self.stripOutJunk(allProducts)

    def getAllBrandsFromIdenticalProducts(self, theProduct):
        '''Gather every brand from the dataset that has the given product'''
        allBrandsFromIdenticalProducts = self.queryRequest("SELECT brandName FROM products WHERE productName=%s", theProduct)
        return self.stripOutJunk(allBrandsFromIdenticalProducts)
    
    def getIngredients(self, theProduct):
        '''Gathers the list of ingredients from the given product'''
        allIngredients = self.queryRequest("SELECT ingredients FROM products WHERE productName=%s", theProduct)
        #print("Printing all ingredients: ", allIngredients)
        return allIngredients

    def getIngredientsByIdNumber(self, productIdNumber):
        '''Gathers the list of ingredients from the given product'''
        allIngredients = self.queryRequest("SELECT ingredients FROM products WHERE idNumber=%s", productIdNumber)
        print("Printing all ingredients: ", allIngredients)
        return allIngredients

    def getProductByIdNumber(self, productIdNumber):
        '''Retrieves a product given a unique idNumber'''
        theProduct = self.queryRequest("SELECT productName FROM products WHERE idNumber=%s", productIdNumber)
        #print(f"Printing the product associated with {productIdNumber}: {theProduct}")
        return theProduct

    def getBrandByIdNumber(self, idNumber):
        "Retreives a brand title given the ID number of a product"
        brand = self.queryRequest("SELECT brandName FROM products WHERE idNumber=%s", idNumber)
        print(f"Printing the brand associated with {idNumber}: {brand}")

        return brand 

if __name__ == '__main__':
    my_source = DataSource()
    my_source.connect()
    my_source.getProducts("G. T. Japan, Inc.")
    # my_source.getAllProducts()
    # my_source.getIngredients("PIGS LIPS")
    # my_source.getProductByIdNumber("45331214")
    # my_source.getBrandByIdNumber("45331214")
    # my_source.getIngredientsByIdNumber("45331214")
