import mysql.connector
import credentials as cred


def create_order(order):
    """Connect to database and insert new order. Each item in order list is put in its own row in database"""

    #  connect to database
    mydb = mysql.connector.connect(
        host="localhost",
        user=cred.user,
        passwd=cred.password,
        database="coffee_test"
    )

    #  create cursor
    mycursor = mydb.cursor()

    #  sql command to insert new row in current_orders table
    sql = "INSERT INTO current_orders (tbl, item, price) VALUES (%s, %s, %s)"
    #  execute many to add each item in passed order list
    mycursor.executemany(sql, order)
    #  commit changes
    mydb.commit()


def get_orders():
    """Connect to database and display orders"""
    mydb = mysql.connector.connect(
        host="localhost",
        user=cred.user,
        passwd=cred.password,
        database="coffee_test"
    )

    mycursor = mydb.cursor()

    #  select everything in current_orders table
    mycursor.execute("SELECT * FROM current_orders")
    orders = mycursor.fetchall()
    for o in orders:
        print(o)
