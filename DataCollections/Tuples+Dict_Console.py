Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = (4,6,5,7,7,3)
>>> type(x)
<class 'tuple'>
>>> x[0] = 10
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x[0] = 10
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> x = 12
>>> x = 12,
>>> x
(12,)
>>> x = 12,34,657,67
>>> x
(12, 34, 657, 67)
>>> emp = name,age,sal,dept = 'Ram',45,45000,'IT'
>>> emp
('Ram', 45, 45000, 'IT')
>>> name
'Ram'
>>> age
45
>>> sal
45000
>>> dept
'IT'
>>> age = 55
>>> age
55
>>> emp
('Ram', 45, 45000, 'IT')
>>> emp = {"name":"Ram","age":45,"sal":45000,"dept":"IT"}
>>> emp
{'name': 'Ram', 'age': 45, 'sal': 45000, 'dept': 'IT'}
>>> emp[0]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    emp[0]
KeyError: 0
>>> emp.keys()
dict_keys(['name', 'age', 'sal', 'dept'])
>>> emp.values()
dict_values(['Ram', 45, 45000, 'IT'])
>>> emp.items()
dict_items([('name', 'Ram'), ('age', 45), ('sal', 45000), ('dept', 'IT')])
>>> emp['name']
'Ram'
>>> emp["address"] = "Delhi"
>>> emp
{'name': 'Ram', 'age': 45, 'sal': 45000, 'dept': 'IT', 'address': 'Delhi'}
>>> emp.update('name','Raman')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    emp.update('name','Raman')
TypeError: update expected at most 1 arguments, got 2
>>> emp.update('name') = 'Ram'
SyntaxError: can't assign to function call
>>> emp.update('name')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    emp.update('name')
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> emp.update(['name'])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    emp.update(['name'])
ValueError: dictionary update sequence element #0 has length 4; 2 is required
>>> emp["address"] = "Pune"
>>> emp
{'name': 'Ram', 'age': 45, 'sal': 45000, 'dept': 'IT', 'address': 'Pune'}
>>> emp.get("name")
'Ram'
>>> emp["gender"]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    emp["gender"]
KeyError: 'gender'
>>> emp.get("gender")
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/DataCollections/02-DictionaryCode.py 
{'name': 'Aman', 'age': 34, 'sal': 55000, 'dept': 'HR'}
{'name': 'Roma', 'age': 45, 'sal': 55000, 'dept': 'IT'}
{'name': 'Shyam', 'age': 41, 'sal': 40000, 'dept': 'HR'}
{'name': 'Geeta', 'age': 39, 'sal': 29000, 'dept': 'IT'}
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/DataCollections/02-DictionaryCode.py 
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/DataCollections/02-DictionaryCode.py", line 25, in <module>
    print(data["name"],data["dept"],data["sal"])
KeyError: 'name'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/DataCollections/02-DictionaryCode.py 
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/DataCollections/02-DictionaryCode.py", line 25, in <module>
    print(data["name"],data["dept"],data["sal"])
KeyError: 'name'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/DataCollections/02-DictionaryCode.py 
['Ram', 'Shyam', 'Gopal', 'Mohan', 'Mohini', 'Sita', 'Geeta'] ['IT', 'HR', 'SALES', 'HR', 'IT', 'IT', 'HR'] [45000, 43000, 29000, 28000, 33000, 37000, 42000]
['Ram', 'Shyam', 'Gopal', 'Mohan', 'Mohini', 'Sita', 'Geeta'] ['IT', 'HR', 'SALES', 'HR', 'IT', 'IT', 'HR'] [45000, 43000, 29000, 28000, 33000, 37000, 42000]
['Ram', 'Shyam', 'Gopal', 'Mohan', 'Mohini', 'Sita', 'Geeta'] ['IT', 'HR', 'SALES', 'HR', 'IT', 'IT', 'HR'] [45000, 43000, 29000, 28000, 33000, 37000, 42000]
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/DataCollections/02-DictionaryCode.py 
Ram IT 45000
Mohini IT 33000
Sita IT 37000
>>> import pandas as pd
>>> pd.DataFrame(data)
    names   dept    sal
0     Ram     IT  45000
1   Shyam     HR  43000
2   Gopal  SALES  29000
3   Mohan     HR  28000
4  Mohini     IT  33000
5    Sita     IT  37000
6   Geeta     HR  42000
>>> df = pd.DataFrame(data)
>>> import matplotlib.pyplot as plt
>>> plt.bar(df["names"], df["sal"])
<BarContainer object of 7 artists>
>>> plt.show()
>>> 
