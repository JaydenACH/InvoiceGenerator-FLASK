import sqlite3
from backendprocess import showcurrency


def insert_currency(sym: str, desc: str, def_curr: int = 0, dis_curr: int = 1):
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO currency VALUES 
                    (?, ?, ?, ?, ?)""", (None, sym, desc, def_curr, dis_curr))


def update_currency(sym: str):
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        results = showcurrency()
        for result in results:
            if result[1] == sym:
                cur.execute("""UPDATE currency SET default_curr=1 WHERE symbol=?;""", (sym,))
            else:
                cur.execute("""UPDATE currency SET default_curr=0 WHERE symbol=?;""", (result[1],))


def update_displaycurrency(syms: list):
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        results = showcurrency()
        for result in results:
            if result[1] in syms:
                cur.execute("""UPDATE currency SET display_curr=1 WHERE symbol=?;""", (result[1],))
            else:
                cur.execute("""UPDATE currency SET display_curr=0 WHERE symbol=?;""", (result[1],))


def delete_currency(sym):
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""DELETE FROM currency WHERE symbol=?;""", (sym,))


def insert_customer(name: str, address: str, telephone: str):
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO customers VALUES
                    (?, ?, ?, ?)""", (None, name, address, telephone))


def delete_customer(cus_id: int):
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""DELETE FROM customers WHERE id=?;""", (cus_id,))


def insert_projects(title: str, customer: str, currency: int, date_created: str, date_modified: str,
                    payment_term: int, total_amount: float, total_received: float, swiftcode: int):
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO projects VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (None, title, customer, currency, date_created, date_modified,
                     payment_term, total_amount, total_received, swiftcode))


def insert_quotation(proj_id: int, desc: str, rev: int):
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO quotation VALUES 
                    (?, ?, ?, ?)""", (None, proj_id, desc, rev))


def insert_itemdetails(proj_id: int, desc: str, qty: int, uom: str, unitprice: float):
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO itemdetails VALUES 
                    (?, ?, ?, ?, ?, ?)""", (None, proj_id, desc, qty, uom, unitprice))


def insert_invoice(proj_id: int, weightage: int, remark: str, date_issued: str):
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO invoice VALUES 
                    (?, ?, ?, ?, ?)""", (None, proj_id, weightage, remark, date_issued))


def update_customer():
    pass


def update_invoice():
    pass


def update_itemdetails():
    pass


def update_projects():
    pass


def update_quotation():
    pass
