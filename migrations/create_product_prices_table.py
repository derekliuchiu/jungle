import mysql.connector
from mysql.connector import Error

try:
    establish_con = mysql.connector.connect(
                    host="127.0.0.1",
                    database = 'prices',
                    port=3306,
                    user="root",
                    password="#eW2IV0pK&rH9&R65*IO"
                    )
    db_Info = establish_con.get_server_info()
    print("Connected to MySQL Server ", db_Info)
    #Create Cursor Object,prepared = True is best practice
    mycursor = establish_con.cursor(prepared=True)
    mycursor.execute("select database();")
    db = mycursor.fetchone()
    print("Connected to database: ", db)
    #Now Create a Toyota for example
    Query = """
            CREATE TABLE ProductPrices(
            Id Int(11) NOT NULL AUTO_INCREMENT,
            Asin varchar(255) NOT NULL,
            Price DECIMAL(5,2) NOT NULL,
            Date Int(11) NOT NULL,
            PRIMARY KEY (Id)
            ) 
            """
    MyQuerry = mycursor.execute(Query)
 
    print("Table created")
    establish_con.commit()
    mycursor.close()
    establish_con.close()
except Error as err:
    print("Connection error to MySQL", err)
