import mysql.connector

class MySQL:
    host = "127.0.0.1"
    port=3306
    user = "root"
    def __init__(self, database, password):
        establish_con = mysql.connector.connect(
                    host = MySQL.host,
                    database = database,
                    port= MySQL.port,
                    user= MySQL.user,
                    password=password
                    )
        self.connection = establish_con
        self.cursor = self.connection.cursor()

    def get_price_date(self, asin, time):
        dic = {}
        query = "SELECT Price, FROM_UNIXTIME(Date) FROM ProductPrices WHERE Asin = %s"
        asin_val = (asin,)
        print(asin)
        self.cursor.execute(query, asin_val)
        records = self.cursor.fetchall()
        for price, date in records:
            dic[str(date)] = str(price)
        return dic
    
    def __del__(self):
        self.cursor.close()
        self.connection.close()




