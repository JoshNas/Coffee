import mysql.connector
import credentials as cred


def create_order(order):
    mydb = mysql.connector.connect(
        host="localhost",
        user=cred.user,
        passwd=cred.password,
        database="coffee_test"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO current_orders (tbl, item, price) VALUES (%s, %s, %s)"
    mycursor.executemany(sql, order)

    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def get_orders():
    mydb = mysql.connector.connect(
        host="localhost",
        user=cred.user,
        passwd=cred.password,
        database="coffee_test"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM current_orders")
    orders = mycursor.fetchall()
    for o in orders:
        print(o)