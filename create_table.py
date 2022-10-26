import sqlite3

conn = sqlite3.connect('p1_database.db')
cur = conn.cursor()

# with conn: 
#     cur.execute("""CREATE TABLE currency (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     symbol TEXT,
#                     description TEXT,
#                     default_curr INTEGER,
#                     display_curr INTEGER
#                 )""")

# with conn:
#     cur.execute("""CREATE TABLE projects (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     title TEXT,
#                     customer TEXT,
#                     currency INTEGER,
#                     date_created TEXT,
#                     date_modified TEXT,
#                     payment_term TEXT,
#                     total_amount REAL,
#                     total_received REAL,
#                     swiftcode INTEGER
#                 )""")

# with conn:
#     cur.execute("""CREATE TABLE quotation (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     proj_id INTEGER,
#                     date_issued TEXT,
#                     revision INTEGER
#                 )""")
    
# with conn:
#     cur.execute("""CREATE TABLE itemdetails (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     proj_id INTEGER,
#                     description TEXT,
#                     quantity INTEGER,
#                     uom TEXT,
#                     unit_price REAL
#                 )""")

# with conn:    
#     cur.execute("""CREATE TABLE invoice (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     proj_id INTEGER,
#                     weightage INTEGER,
#                     remark TEXT,
#                     date_issued TEXT
#                 )""")

# with conn:     
#     cur.execute("""CREATE TABLE customers (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT,
#                     address TEXT,
#                     telephone TEXT
#                 )""")
    
    