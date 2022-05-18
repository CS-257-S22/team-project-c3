# from colorama import Cursor
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

    def getProducts(self, brand):
        '''Gather the products associated with the given brandName'''

        cursor = self.theConnection.cursor()

        query = "SELECT productName FROM products WHERE brandName=%s"

        cursor.execute(query, (brand,))

        print(cursor.fetchall())

if __name__ == '__main__':
    my_source = DataSource()
    my_source.connect()
    my_source.getProducts("ACME MARKETS")