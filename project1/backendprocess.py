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