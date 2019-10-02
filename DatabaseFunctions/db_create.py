import mysql.connector
from DatabaseFunctions import credentials as cred

mydb = mysql.connector.connect(
    host="localhost",
    user=cred.user,
    passwd=cred.password,
    database="coffee_test"
)

mycursor = mydb.cursor()

#  mycursor.execute("CREATE DATABASE CoffeeTest")
# mycursor.execute("DROP TABLE current_orders")
mycursor.execute("CREATE TABLE current_orders (id INT AUTO_INCREMENT PRIMARY KEY, "
                 "tbl VARCHAR(100),item VARCHAR(100), price FLOAT)")
