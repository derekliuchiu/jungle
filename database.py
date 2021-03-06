import mysql.connector

class MySQL:

    host = "127.0.0.1"
    port = 3306
    user = "root"

    def __init__(self, database, password):
        self.database = database
        self.password = password
        # if error occurs during mysql connection, __del__ shouldnt try to close
        self.connection = mysql.connector.connect(
            host = MySQL.host,
            database = self.database,
            port = MySQL.port,
            user = MySQL.user,
            password = self.password,
            autocommit = True
        )
        self.cursor = self.connection.cursor()

    def get_price_date(self, asin): #took out time parameter
        query = "SELECT Price, FROM_UNIXTIME(Date) FROM ProductPrices WHERE Asin = %s"
        asin_val = (asin,)
        self.cursor.execute(query, asin_val)
        records = self.cursor.fetchall()
        dic = {}
        for price, date in records:
            dic[str(date)] = str(price)
        return dic
    
    def insert_product(self, asin):
        query = "INSERT INTO Products VALUES (%s) ON DUPLICATE KEY UPDATE Asin = Asin"
        values = (asin,)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_product_table(self):
        query = "SELECT * FROM Products"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        res = [x[0] for x in records]
        return res
    
    def insert_to_prices(self, asin, price):
        query = "INSERT INTO ProductPrices (Asin, Price, Date) VALUES (%s, %s, UNIX_TIMESTAMP()) ON DUPLICATE KEY UPDATE Price=VALUES(Price)"
        values = (asin, price)
        self.cursor.execute(query, values)
        self.connection.commit()
        #print(self.cursor.rowcount, "record inserted")


    def __del__(self):
        self.cursor.close()
        self.connection.close()
