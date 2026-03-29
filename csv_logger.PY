import csv
from datetime import datetime

def log_items(items, filename="items.csv"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = 0
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Timestamp"])
        writer.writerow([now])

        writer.writerow(["name", "price"])

        for item in items:
            writer.writerow([item["name"], item["price"]])
            total += item["price"]

        writer.writerow([])
        writer.writerow(["Total", total]) 

        
items =[]
while True:
    name = input("enter item name (or 'done' to finish): ")
    if name.lower() == "done":
        break
    price = float(input("enter item price: "))
    items.append({"name": name, "price": price})

log_items(items)