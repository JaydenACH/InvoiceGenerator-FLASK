import sqlite3
from backendprocess import getcurrbyid, getcusnamebyid, showcurrency


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


def insert_projects(projid:int, title: str, cusid: int, currency: int, date_created: str, date_modified: str,
                    payment_term: str, total_amount: float, total_received: float, swiftcode: bool):
    cusname = getcusnamebyid(cusid)
    sc = 1 if swiftcode else 0
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO projects VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (None, projid, title, cusname, currency, date_created, date_modified,
                     payment_term, total_amount, total_received, sc))


def insert_quotation(quo_id: str, proj_id: int, issdate: str, rev: int):
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO quotation VALUES 
                    (?, ?, ?, ?, ?)""", (None, quo_id, proj_id, issdate, rev))


def insert_itemdetails(proj_id: int, desc_list: list, qty_list: list, uom_list: list, unitprice_list: list):
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        for desc, qty, uom, unitprice in zip(desc_list, qty_list, uom_list, unitprice_list):
            cur.execute("""INSERT INTO itemdetails VALUES 
                        (?, ?, ?, ?, ?, ?)""", (None, proj_id, desc, qty, uom, unitprice))


def insert_invoice(inv_id: str, proj_id: int, weightage_list: int, remark_list: str, date_issued: str):
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        for weightage, remark in zip(weightage_list, remark_list):
            cur.execute("""INSERT INTO invoice VALUES 
                        (?, ?, ?, ?, ?, ?)""", (None, inv_id, proj_id, weightage, remark, date_issued))


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
