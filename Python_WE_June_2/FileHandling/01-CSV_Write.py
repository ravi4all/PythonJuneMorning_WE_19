import csv
# comma seperated values

products = [
    {"head_1":"Names","head_2":"Price"},
    {"name":"Apple","p_price":45000},
    {"name":"Redmi","p_price":15000},
    {"name":"Apple","p_price":49000},
    {"name":"Samsung","p_price":65000},
    {"name":"Apple","p_price":98000},
]

with open('products.csv','w', newline='') as file:
    write = csv.writer(file)
    for item in products:
        write.writerow(item.values())