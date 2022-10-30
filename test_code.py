from email import header
from backendprocess import showcurrency, showcustomer, showitemdetails, showproject, showquotation, showterms, showinvoice
from tabulate import tabulate

# testing for backend process code


# Print out SQL tables for checking
print("showproject__________________________________________________________________________________________________")

print(tabulate(showproject(), headers=["id", "proj_id", "title", "customer", "currency", 
                                        "created", "modified", "payment term", 
                                        "total amount", "total received", "swift"]))
print("\nshowcurrency__________________________________________________________________________________________________")
print(tabulate(showcurrency(), headers=["id", "symbol", "desc", "default", "display"]))
print("\nshowcustomer__________________________________________________________________________________________________")
print(tabulate(showcustomer(), headers=["id", "name", "address", "telephone"]))
print("\nshowquotation__________________________________________________________________________________________________")
print(tabulate(showquotation(), headers=["id", "quo_id", "proj_id", "issue", "rev"]))
print("\nshowinvoice__________________________________________________________________________________________________")
print(tabulate(showinvoice(), headers=["id", "inv_id", "proj_id", "weightage", "remark", "issued"]))
print("\nshowitemdetails__________________________________________________________________________________________________")
print(tabulate(showitemdetails(), headers=["id", "proj_id", "desc", "qty", "uom", "unitprice"]))
