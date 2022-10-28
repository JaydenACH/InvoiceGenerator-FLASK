import sqlite3


def showcurrency():
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""SELECT * FROM currency;""")
        
    return cur.fetchall()


def showcustomer():
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""SELECT * FROM customers;""")
        
    return cur.fetchall()


def showterms():
    return ["7 days", "30 days", "C.O.D."]


def calculate_totalamount(qty: list, unitprice: list) -> float:
    return 0.00