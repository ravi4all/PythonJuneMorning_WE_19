'''
data = [
    {"name":'Ram',"age":30,"sal":45000,"dept":"IT"},
    {"name":'Aman',"age":34,"sal":55000,"dept":"HR"},
    {"name":'Raman',"age":29,"sal":49000,"dept":"IT"},
    {"name":'Roma',"age":45,"sal":55000,"dept":"IT"},
    {"name":'Shyam',"age":41,"sal":40000,"dept":"HR"},
    {"name":'Geeta',"age":39,"sal":29000,"dept":"IT"},
    ]

for emp in data:
    if emp["age"] > 30:
        print(emp)
'''

data = {
    "names" : ["Ram","Shyam","Gopal","Mohan","Mohini","Sita","Geeta"],
    "dept" : ["IT","HR","SALES","HR","IT","IT","HR"],
    "sal" : [45000,43000,29000,28000,33000,37000,42000]
    }


for i in range(len(data["dept"])):
    if data["dept"][i] == "IT":
        print(data["names"][i],data["dept"][i],data["sal"][i])
