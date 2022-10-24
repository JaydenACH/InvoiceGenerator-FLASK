from audioop import add
import sqlite3

conn = sqlite3.connect('p1_database.db')
cur = conn.cursor()


def insert_currency(sym:str , desc:str , def_curr:int , dis_curr:int):
    with conn:
        cur.execute("""INSERT INTO currency VALUES 
                    (%s, %s, %s, %s)""", (sym, desc, def_curr, dis_curr))
        

def insert_customer(name:str , address:str , telephone:str):
    with conn:
        cur.execute("""INSERT INTO customers VALUES
                    (%s, %s, %s)""", (name, address, telephone))
        
        
def insert_projects(title: str, customer: str, currency: int, date_created:str, date_modified:str, 
                    payment_term: int, total_amount: float, total_received: float, swiftcode: int):
    with conn:
        cur.execute("""INSERT INTO projects VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                    (title, customer, currency, date_created, date_modified,
                     payment_term, total_amount, total_received, swiftcode))
        
        
def insert_quotation(proj_id: int, desc: str, rev: int):
    with conn: 
        cur.execute("""INSERT INTO quotation VALUES 
                    (%s, %s, %s)""", (proj_id, desc, rev))
    

def insert_itemdetails(proj_id: int, desc: str, qty: int, uom:str, unitprice: float):
    with conn: 
        cur.execute("""INSERT INTO itemdetails VALUES 
                    (%s, %s, %s, %s, %s)""", (proj_id, desc, qty, uom, unitprice))


def insert_invoice(proj_id: int, weightage: int, remark: str, date_issued: str):
    with conn: 
        cur.execute("""INSERT INTO invoice VALUES 
                    (%s, %s, %s, %s)""", (proj_id, weightage, remark, date_issued))
        
        
def update_currency():
    pass

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