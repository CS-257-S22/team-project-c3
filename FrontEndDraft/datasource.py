import psycopg2
import psqlConfig as config

class DataSource:

    def __init__(self):
        self.theConnection = self.connect()
        pass

    def connect(self):
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def stripCommas(self, rawDataTuples):
        '''Strip out the leading and trailing parantheses and apostrophes
        WORK IN PROGRESS'''
        # rawDataString = ''.join([str(item) for item in rawDataList])
        # print(rawDataString)
        # rawDataList = list(rawDataTuples)
        # rawDataString = rawDataString.replace("(", "")
        # rawDataString = rawDataString.replace("'", "")
        # rawDataString = rawDataString.replace(")", "")
        # print(rawDataString)
        # for aTuple in rawDataTuples:

        # print(rawDataTuples)
        # for component in rawDataList:
        #     component = component.strip(",")
        
        # strippedDataList = rawDataString.strip(",")
      #  strippedDataList = []
       # for item in rawDataTuples:
        #    strippedDataList.append(str(item))

        #for item in strippedDataList:
         #   item = item.replace("(", '')
          #  item = item.replace("'", '')
           # item = item.replace(")", '')
            # appenedItem = item[2: item.length()]
       # return strippedDataList

    def stripProducts(self, products):
        '''Strip the prodcuts of leading parantheses and apostrophes'''
        return self.stripCommas(products)

    def getProducts(self, brand):
        '''Gather the products associated with the given brandName'''

        cursor = self.theConnection.cursor()
        query = "SELECT productName FROM products WHERE brandName=%s"
        cursor.execute(query, (brand,))
        brandProducts = (cursor.fetchall())
        return brandProducts
      #  return self.stripProducts(brandProducts)

    def getAllProducts(self):
        '''Gather every product name included in the dataset'''

        cursor = self.theConnection.cursor()
        query = "SELECT productName FROM products"
        cursor.execute(query,)
        allProducts = (cursor.fetchall())
        return allProducts
        #return self.stripProducts(allProducts)
    
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
    print(my_source.getProducts("Holiday Candy Corp, Inc."))
    print(my_source.getIngredients("JELLY WREATHS"))