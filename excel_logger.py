import openpyxl
from datetime import datetime 

def log_items(items, filename="Products.xlsx"):
    wb  = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Items"

    #TimeStamp
    ws.append(["Timestamp", datetime.now()])
    ws.append([])

    #Headers
    ws.append(["Name", "Price"])

    #Items
    total = 0
    for item in items:
        ws.append([item["name"], item["price"]])
        total += item["price"]

    #Total
    ws.append([])
    ws.append(["Total", round(total, 2)])

    wb.save(filename)
    print(f"Saved to {filename}")


items = []
while True:
    name = input("Item name (or 'done'): ")
    if name.lower() == "done": 
        break
    price = float(input("Price: "))
    items.append({"name": name, "price": price})

log_items(items)