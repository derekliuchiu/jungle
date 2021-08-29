import mysql.connector
from mysql.connector import Error

try:
    establish_con = mysql.connector.connect(
                    host="127.0.0.1",
                    port=3306,
                    user="root",
                    password="#eW2IV0pK&rH9&R65*IO"
                    )
    db_Info = establish_con.get_server_info()
    print("Connected to MySQL Server ", db_Info)
    #Create Cursor Object,prepared = True is best practice
    mycursor = establish_con.cursor(prepared=True)
    mycursor.execute("CREATE DATABASE Prices")
    mycursor.execute("SHOW DATABASES")
    databases = mycursor.fetchall()
    print(databases)
    mycursor.close()
    establish_con.close()

except Error as err:
    print("Connection error to MySQL", err)
