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
        '''
        PARAMETER: N/A
        RETURN: returns connection to SQL query
        PURPOSE: Creates a connection to the products database
        '''

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


    def queryRequest(self, theQueryString, secondaryArgumentString, tertiaryArgumentString):
        '''
        PARAMETER: theQueryString: string of the query that will be executed
        PARAMETER: secondaryArgumentString: the secondary parameter for the query. Not all queries use it. 
        RETURN:    Returned value of query executed
        PURPOSE:   Facilitate the query request to the database. Can be utilized w/ or w/out a 
        secondary argument. Returns the fetched data.
        ATTENTION: If the secondaryArgumentString is None, then so should the tertiaryArgumentString!!
        '''
        cursor = self.theConnection.cursor()
        if None == secondaryArgumentString:
            cursor.execute(theQueryString,)
        elif None != tertiaryArgumentString:
            cursor.execute(theQueryString, (secondaryArgumentString, tertiaryArgumentString,))
        else:
            cursor.execute(theQueryString, (secondaryArgumentString,))
        return (cursor.fetchall())

    def stripProducts(self, products):
        '''
        PARAMETER: products: un-stripped list of products with lots of extra characters that need to go. 
        RETURN:    product list where each item is a stripped string
        PURPOSE:   Strip the prodcuts of leading parantheses and apostrophes
        '''
       
        return self.stripOutJunk(products)


    def getProducts(self, brand):
        '''
        PARAMETER: brand: brand getting passed into query     
        RETURN: stripped productes of queryRequest with brand 
        PURPOSE:  Gather the products associated with the given brandName  
        '''
        brandProducts = self.queryRequest("SELECT productName FROM products WHERE brandName=%s", brand, None)
        print("Printing brand products: ", brandProducts)
        return self.stripOutJunk(brandProducts)

    def getAllProducts(self):
        '''
        PARAMETER  N/A     
        RETURN:   Every product name in the dataset 
        PURPOSE: Gather every product name included in the dataset
        '''
        allProducts = self.queryRequest("SELECT productName FROM products", None, None)
        # print("Printing all products: ", allProducts)
        return self.stripOutJunk(allProducts)

    def getAllBrandsFromIdenticalProducts(self, theProduct):
        '''
        PARAMETER: theProduct: the product of which the query is looking for 
        RETURN: all brands that have a product that matches theProduct
        PURPOSE: Query to find all brand names that have the same product name as a given product
        '''
        print("Now in datasource and about to attempt query for getAllBrandsFromIdenticalProducts.")
        allBrandsFromIdenticalProducts = self.queryRequest("SELECT brandName FROM products WHERE productName=%s", theProduct, None)
        print(allBrandsFromIdenticalProducts)
        return self.stripOutJunk(allBrandsFromIdenticalProducts)
    
    def getIngredients(self, theProduct, theBrand):
        '''
        PARAMETER:  theProduct:   desired product that query will search for 
        PARAMETER: theBrand: the brand associated with the desired product
        RETURN:     ingredients that query retrieved
        PURPOSE:    Gathers a list of ingredients from the given product
        '''
        print("The product: ", theProduct, " The brand: ", theBrand)
        allIngredients = self.queryRequest("SELECT ingredients FROM products WHERE productName=%s AND brandName=%s", theProduct, theBrand)
        print("Printing all ingredients: ", allIngredients)
        return allIngredients

    def getIngredientsByIdNumber(self, productIdNumber):
        '''
        PARAMETER: productIdNumber: id number of the product we are searching for 
        RETURN: Name of product that corresponds to product 
        PURPOSE: Gathers the ingredients by looking for it’s ID number 
        '''
        allIngredients = self.queryRequest("SELECT ingredients FROM products WHERE idNumber=%s", productIdNumber, None)
        print("Printing all ingredients: ", allIngredients)
        return allIngredients

    def getProductByIdNumber(self, productIdNumber):
        '''
        PARAMETER: productIdNumber: Id number of the product we are looking for 
        RETURN: returns the product to the corresponding ID
        PURPOSE: Query that looks for product name that matches the ID number 
        '''
        theProduct = self.queryRequest("SELECT productName FROM products WHERE idNumber=%s", productIdNumber, None)
        #print(f"Printing the product associated with {productIdNumber}: {theProduct}")
        return theProduct

    def getBrandByIdNumber(self, idNumber):
        '''
        PARAMETER: idNumber: returns brandname of the product whose id number matches that of the parameter
        RETURN: Retrieves a brand title given the Id number of the product       
        PURPOSE: runs a query to find brand through a product's id number 
        '''
        brand = self.queryRequest("SELECT brandName FROM products WHERE idNumber=%s", idNumber, None)
        print(f"Printing the brand associated with {idNumber}: {brand}")

        return brand 
    def getSearchBarMatches(self, search):
        matches = self.queryRequest("SELECT * FROM products WHERE product CONTAINS %s",search, None)
        print(f"Printing the matches associated with {search}")
        return matches

if __name__ == '__main__':
    my_source = DataSource()
    my_source.connect()
    
   
