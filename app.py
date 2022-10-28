from flask import Flask, flash, render_template, request, redirect
from db_query import delete_currency, delete_customer, insert_currency, insert_customer, insert_invoice, \
    insert_itemdetails, insert_projects, insert_quotation, update_currency, update_customer, update_displaycurrency, \
    update_invoice, update_itemdetails, update_projects, update_quotation
from backendprocess import calculate_totalamount, showcurrency, showcustomer, showterms
from datetime import datetime


app = Flask(__name__)
app.config["SECRET_KEY"] = "lsdjbkcklvzjbdvilabjewdib122ug3ef"
app.config["TEMPLATES_AUTO_RELOAD"] = True


# class SalesProject:
#     def __init__(self, currency: int, payment_term: int, swift_code: int) -> None:
#         self.title = request.form.get("title").strip().title()
#         self.customer = request.form.get("customer").strip()
#         self.currency = currency
#         self.date_created = datetime.today()
#         self.date_modified = ""
#         self.payment_term = payment_term
#         self.total_amount = request.form.get("total_amount")
#         self.total_received = 0
#         self.balance = self.total_amount - self.total_received
#         self.swift_code = swift_code

#     def __str__(self):
#         return f"Project: {self.title} by {self.customer} is bringing in {self.currency}{self.total_amount}."


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")


@app.route("/settings-customer", methods=["POST", "GET"])
def settingscustomer():
    results = showcustomer()
    if request.method == "GET":
        return render_template("settings-customer.html", results=results)
    else:
        cus_name = request.form.get("newcustomer")
        cus_add = request.form.get("newaddress")
        cus_tel = request.form.get("newtelephone")
        insert_customer(cus_name, cus_add, cus_tel)
        return redirect("/settings-customer")


@app.route("/deletecustomer", methods=["GET", "POST"])
def deletecustomer():
    if request.method == "POST":
        cus_id = request.form.get("customer")
        delete_customer(int(cus_id))
        return redirect("/settings-customer")
    
        
@app.route("/settings-currency", methods=["GET", "POST"])
def settings():
    results = showcurrency()
    if request.method == "GET":
        return render_template("settings-currency.html", results=results)
    else:
        sym = request.form.get("newsymbol")
        desc = request.form.get("description")
        for result in results:
            if sym == result[1]:
                flash("Currency existed!", "error")
                return redirect("/settings-currency")
        insert_currency(sym, desc, 0, 1)
        return redirect("/settings-currency")


@app.route("/setdefcurrency", methods=["GET", "POST"])
def setdefault():
    if request.method == "POST":
        sym = request.form.get("currency")
        update_currency(sym)
        return redirect("/settings-currency")


@app.route("/newproject", methods=["GET", "POST"])
def newproject():
    if request.method == "GET":
        return render_template("newproject.html", currency=showcurrency(),
                               terms=showterms(), customer=showcustomer())
    else:
        projectid = request.form.get("project-id").strip()
        projecttitle = request.form.get("project-title").strip().title()
        projectcurrency = request.form.get("project-currency")
        projectterms = request.form.get("project-terms")
        swiftcode = request.form.get("swiftcode") != None
        customerid = request.form.get("customer-id")
        itemdesc = request.form.get("item-description[]")
        itemqty = request.form.getlist("item-quantity[]")
        itemuom = request.form.getlist("item-uom[]")
        itemunitprice = request.form.getlist("item-unitprice[]")
        issuedate = request.form.get("issuedate")
        paypercent = request.form.getlist("percent[]")
        payremark = request.form.getlist("remark[]")
        # totalamount = calculate_totalamount(itemqty, itemunitprice)
        # insert_projects(projecttitle, customerid, projectcurrency, str(datetime.today()), "", projectterms, totalamount, "", swiftcode)
        # insert_quotation(projectid, itemdesc, 0)
        # insert_itemdetails(projectid, itemdesc, itemqty, itemuom, itemunitprice)
        # insert_invoice(projectid, paypercent, payremark, issuedate)
        flash("The project will not be recorded yet, as the feature is not completed in backend", "info")
        return render_template("newproject.html")


@app.route("/deletecurrency", methods=["POST", "GET"])
def deletecurrency():
    if request.method == "POST":
        sym = request.form.get("symbol")
        delete_currency(sym)
        return redirect("/settings-currency")


@app.route("/setdisplaycurrency", methods=["POST", "GET"])
def setdisplaycurrency():
    if request.method == "POST":
        sym = request.form.getlist("symbol")
        update_displaycurrency(sym)
        return redirect("/settings-currency")


if __name__ == "__main__":
    app.run()
