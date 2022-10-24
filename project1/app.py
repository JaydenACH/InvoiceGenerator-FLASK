from flask import Flask, render_template, request
from datetime import datetime
from db_query import insert_currency, insert_customer, insert_invoice, insert_itemdetails, insert_projects, insert_quotation, update_currency, update_customer, update_invoice, update_itemdetails, update_projects, update_quotation

app = Flask(__name__)



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

    

@app.route("/")
def index():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/settings")
def settings():
    if request.method == "GET":
        return render_template("settings.html")
    else:
        mode = request.form.get("mode")
        if mode == "new":
            sym = request.form.get("symbol")
            desc = request.form.get("description")
            def_curr = request.form.get("def_curr")
            dis_curr = request.form.getlist("display_currency")
            insert_currency(sym, desc, def_curr, dis_curr)
        else:
            
            update_currency()

if __name__ == "__main__":
    app.run(debug=True)