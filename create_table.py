import sqlite3


conn = sqlite3.connect('p1_database.db')
cur = conn.cursor()

def create_projects():
    with conn:
        cur.execute("""DROP TABLE IF EXISTS projects""")
        cur.execute("""CREATE TABLE projects (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        proj_id TEXT,
                        title TEXT,
                        customer TEXT,
                        currency INTEGER,
                        date_created TEXT,
                        date_modified TEXT,
                        payment_term TEXT,
                        total_amount REAL,
                        total_received REAL,
                        swiftcode INTEGER
                    )""")


def create_currency():
    with conn: 
        cur.execute("""CREATE TABLE currency (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        symbol TEXT,
                        description TEXT,
                        default_curr INTEGER,
                        display_curr INTEGER
                    )""")


def create_customers():
    with conn:     
        cur.execute("""CREATE TABLE customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        address TEXT,
                        telephone TEXT
                    )""")


def create_quotation():
    with conn:
        cur.execute("""DROP TABLE IF EXISTS quotation""")
        cur.execute("""CREATE TABLE quotation (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        quo_id TEXT,
                        proj_id TEXT,
                        date_issued TEXT,
                        revision INTEGER
                    )""")
        

def create_invoice():
    with conn:    
        cur.execute("""DROP TABLE IF EXISTS invoice""")
        cur.execute("""CREATE TABLE invoice (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        inv_id TEXT,
                        proj_id TEXT,
                        weightage INTEGER,
                        remark TEXT,
                        date_issued TEXT
                    )""")

    
def create_item_details():
    with conn:
        cur.execute("""DROP TABLE IF EXISTS itemdetails""")
        cur.execute("""CREATE TABLE itemdetails (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        proj_id TEXT,
                        description TEXT,
                        quantity INTEGER,
                        uom TEXT,
                        unit_price REAL
                    )""")


# run this code with caution as it will delete data permanently
if __name__ == "__main__":
    # set the boolean of variables below to True if want to reset the table
    createproject = False
    createitemdetails = False
    createquotation = False
    createinvoice = False
    createcustomer = False
    createcurrency = False
    
    if createproject:
        create_projects()
    if createitemdetails:
        create_item_details()
    if createquotation:
        create_quotation()
    if createinvoice:
        create_invoice()
    if createcustomer:
        create_customers()
    if createcurrency:
        create_currency()
        
    