from flask.templating import render_template
import mysql.connector

class MySQL:

    host = "127.0.0.1"
    port = 3306
    user = "root"

    def __init__(self, database, password):
        self.database = database
        self.password = password
        self.initialized = False
        # if error occurs during mysql connection, __del__ shouldnt try to close
        establish_con = mysql.connector.connect(
            host = MySQL.host,
            database = self.database,
            port = MySQL.port,
            user = MySQL.user,
            password = self.password
        )
        self.connection = establish_con
        self.cursor = self.connection.cursor()
        self.initialized = True

    def get_price_date(self, asin): #took out time parameter
        query = "SELECT Price, FROM_UNIXTIME(Date) FROM ProductPrices WHERE Asin = %s"
        asin_val = (asin,)
        self.cursor.execute(query, asin_val)
        records = self.cursor.fetchall()
        dic = {}
        for price, date in records:
            dic[str(date)] = str(price)
        return render_template("return_product.html", dic = dic)
    
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


    def __del__(self):
        if self.initialized:
            self.cursor.close()
            self.connection.close()
