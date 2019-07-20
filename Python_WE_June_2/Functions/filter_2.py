# def search(data):
#     return data['name'] == 'Apple'

products = [
    {"name":"Apple","p_price":45000},
    {"name":"Redmi","p_price":15000},
    {"name":"Apple","p_price":49000},
    {"name":"Samsung","p_price":65000},
    {"name":"Apple","p_price":98000},
]

# s = list(filter(search, products))
# print(s)

# name = input("Enter your search : ")
# s = list(filter(lambda data : data['name'] == name, products))
# print(s)

# Sorted Data
d = sorted(products, key=lambda x : x['p_price'], reverse=True)
# print(d)
for p in d:
    print(p)