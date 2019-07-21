import csv

data = []
with open('products.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        item = {"name":row[0], "price":row[1]}
        data.append(item)

# print(data)