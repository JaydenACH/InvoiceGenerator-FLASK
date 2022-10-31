import sqlite3
import phonenumbers
from datetime import datetime, timedelta


def showcurrency(key:str = ""):
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


def showproject():
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""SELECT * FROM projects;""")
        
    return cur.fetchall()


def showquotation():
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""SELECT * FROM quotation;""")
        
    return cur.fetchall()


def showitemdetails():
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""SELECT * FROM itemdetails;""")
        
    return cur.fetchall()


def showinvoice():
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""SELECT * FROM invoice;""")
        
    return cur.fetchall()


def checkitementries(itemqty_list: list, itemunitprice_list: list) -> str:
    if len(itemqty_list) != len(itemunitprice_list):
        return ("All quantity & unit price must be provided.", "error")
    
    for item, uprice in zip(itemqty_list, itemunitprice_list):
        if not isinstance(item, (float, int)) or not isinstance(uprice, (float, int)):
            return ("Item entries must be in numbers", "error")

    return ("The project is recorded successfully.", "info")


def checktelephonenumber(tel: str) -> bool:
    return phonenumbers.is_valid_number(tel)


def calculate_totalamount(qtys: list, unitprice: list) -> float:
    total_amount = 0
    for qty, uprice in zip(qtys, unitprice):
        amount = float(qty) * float(uprice)
        total_amount = total_amount + amount
    total_amount = round(total_amount, 2)
    return total_amount


def getcusnamebyid(cusid: int) -> str:
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""SELECT name FROM customers WHERE id=?;""", (cusid))
        
    return cur.fetchone()[0]


def getcurrbyid(currid: int) -> str:
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""SELECT symbol FROM currency WHERE id=?;""", (currid))
        
    return cur.fetchone()

def get_quotationdata() -> list:
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""SELECT * FROM projects;""")
        projects = cur.fetchall()
        cur.execute("""SELECT * FROM quotation;""")
        quotations = cur.fetchall()
        itemcount = {}
        for project in projects:
            cur.execute("""SELECT COUNT(description) FROM itemdetails WHERE proj_id=?;""",
                        (project[1],))
            itemcount[project[1]] = cur.fetchone()[0]
        quotationdata = []
        for project in projects:
            temp_row = []
            temp_row.append(project[1])  #projectid
            temp_row.append(project[2])  #projectname
            temp_row.append(project[3])  #projectcustomer
            temp_row.append(project[8])  #projectamount
            temp_row.append(itemcount[project[1]])  #itemqty
            if quotations:
                for quo in quotations:
                    if quo[1] == project[1]:
                        temp_row.append(quo[0])  #quotationid
                        temp_row.append(quo[2])  #issuedate
                        temp_row.append("")  #validtill
                    else:
                        temp_row.append("")  #blankentry
                        temp_row.append("")  #blankentry
                        temp_row.append("")  #blankentry
            else:
                temp_row.append("")  #blankentry
                temp_row.append("")  #blankentry
                temp_row.append("")  #blankentry
            quotationdata.append(temp_row)
        return {"data": quotationdata}
    
def get_invoicedata():
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""SELECT * FROM projects;""")
        projects = cur.fetchall()
        
        cur.execute("""SELECT * FROM invoice;""")
        invoices = cur.fetchall()
        invoicedata = []
        
        for project in projects:
            for invoice in invoices:
                if project[1] == invoice[2]:
                    temp_row = []
                    temp_row.append(project[1])  #projectid
                    temp_row.append(project[2])  #projectname
                    temp_row.append(project[3])  #projectcustomer
                    temp_row.append(project[8])  #projectamount
                    temp_row.append(invoice[3])  #invoiceweightage
                    temp_row.append(invoice[1])  #invoiceid
                    due = invoice[3] * project[8] / 100
                    temp_row.append(round(due, 2))  #amountdue
                    if invoice[5]: 
                        issuedate = datetime.strptime(invoice[5], '%Y/%m/%d')  #convertdatestringtodateobject
                        try:
                            day, _ = project[7].split(" ")
                            duedate = issuedate + timedelta(days=int(day))  #calculateduedate
                            temp_row.append(duedate)
                        except ValueError:
                            temp_row.append(project[7])
                    else:
                        temp_row.append("")
                    invoicedata.append(temp_row)
        return {"data": invoicedata}
    

def projectidcheck():
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""SELECT proj_id FROM projects;""")
    
    return cur.fetchall()


def provide_defprojid():
    with sqlite3.connect('p1_database.db') as conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(proj_id) FROM projects;""")
        rows = cur.fetchone()[0] + 1
        
        result = projectidcheck()
        if result:
            projid = result[0]
        else:
            projid = "PRJ00001"
            
        while projid in result:
            # max = PRJ99999, for auto generated project number
            # projid format can be further determined by users need 
            if rows > 9999:
                projid = f"PRJ{rows}"  # start from PRJ10000
            elif rows > 999:
                projid = f"PRJ0{rows}"  # start from PRJ01000
            elif rows > 99:
                projid = f"PRJ00{rows}"  # start from PRJ00100
            elif rows > 9:
                projid = f"PRJ000{rows}"  # start from PRJ00010
            else:
                projid = f"PRJ0000{rows}"  # start from PRJ00001
        
        return projid