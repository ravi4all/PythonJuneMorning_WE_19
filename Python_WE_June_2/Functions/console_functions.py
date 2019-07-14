Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/kwargs.py 
ID : 101
Name : Ram
Grade : A
Marks : 45
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/kwargs.py 
Enter your id : 101
Enter your name : Ram
Enter your grade : A+
Enter your marks : 66
ID : 101
Name : Ram
Grade : A
Marks : 45
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/kwargs.py 
Enter your id : 101
Enter your name : Ram
Enter your grade : A
Enter your physics marks : 56
Enter your chemistry marks : 66
Enter your maths marks : 77
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/kwargs.py", line 14, in <module>
    student(id,name,grade,ph_marks,ch_marks,math_marks)
TypeError: student() takes 4 positional arguments but 6 were given
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/kwargs.py 
Enter your id : 101
Enter your name : Ram
Enter your grade : A
Enter your physics marks : 56
Enter your chemistry marks : 77
Enter your maths marks : 54
ID : 101
Name : Ram
Grade : A
Marks : ('56', '77', '54')
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/kwargs.py 
Enter your id : 101
Enter your name : Ram
Enter your grade : A
Enter your physics marks : 67
Enter your chemistry marks : 66
Enter your maths marks : 65
Report Card for Stduent : 101
Hello Ram
Your marks : (67, 66, 65)
Your average marks are 66.0
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/kwargs.py 
Enter your id : 11
Enter your name : Shyam
Enter your grade : B
Enter your physics marks : 45
Enter your chemistry marks : 33
Enter your maths marks : 43
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/kwargs.py", line 21, in <module>
    student(id,name,grade,ph_marks,ch_marks,math_marks)
TypeError: student() missing 2 required keyword-only arguments: 'grade' and 'marks'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/kwargs.py 
{'name': 'Ram', 'age': 14, 'gender': 'm', 'hobby': 'swimming'}
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/kwargs.py 
{'name': 'Ram', 'age': 14, 'gender': 'm', 'hobby': 'swimming'}
{'name': 'Sita', 'age': 15, 'gender': 'f'}
{'name': 'Aman', 'age': 13, 'hobby': 'cricket', 'grade': 'A'}
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/kwargs.py 
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/kwargs.py", line 6, in <module>
    student('Ram',14,'m','swimming')
TypeError: student() takes 0 positional arguments but 4 were given
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/kwargs.py 
('Ram', 14, 'm', 'swimming')
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/kwargs.py", line 7, in <module>
    student(name='Sita',age=15,gender='f')
TypeError: student() got an unexpected keyword argument 'name'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/menuDriven.py 

1. Add
2. Sub
3. Div
4. Mul

Enter your choice : 3
Enter first number : 12
Enter second number : 3
Sum is 123
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/menuDriven.py", line 24, in <module>
    "2" : sub(num_1, num_2),
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/menuDriven.py", line 5, in sub
    z = x - y
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/menuDriven.py 

1. Add
2. Sub
3. Div
4. Mul

Enter your choice : 3
Enter first number : 12
Enter second number : 4
Sum is 16
Diff is 8
Div is 3.0
Mul is 48
>>> def sayHelo():
	print("Hello User")

	
>>> def sayBye():
	print("Bye User")

	
>>> d = {"1":sayHelo(), "2":sayBye()}
Hello User
Bye User
>>> sayHelo
<function sayHelo at 0x00000272B0E1B510>
>>> d = {"1":sayHelo, "2":sayBye}
>>> def sayHelo():
	print("Hello User")
	return "Hey"

>>> def sayBye():
	print("Bye User")
	return Bye

>>> def sayBye():
	print("Bye User")
	return "Bye"

>>> d = {"1":sayHelo(), "2":sayBye()}
Hello User
Bye User
>>> d
{'1': 'Hey', '2': 'Bye'}
>>> d = {"1":sayHelo, "2":sayBye}
>>> d
{'1': <function sayHelo at 0x00000272B0E1B620>, '2': <function sayBye at 0x00000272B0E1B730>}
>>> def sayHelo():
	print("Hello User")

	
>>> def sayBye():
	print("Bye User")

	
>>> d = {"1":sayHelo(), "2":sayBye()}
Hello User
Bye User
>>> d
{'1': None, '2': None}
>>> d = {"1":sayHelo, "2":sayBye}
>>> d
{'1': <function sayHelo at 0x00000272B0E1B510>, '2': <function sayBye at 0x00000272B0E1B598>}
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/menuDriven.py 

1. Add
2. Sub
3. Div
4. Mul

Enter your choice : 3
Enter first number : 12
Enter second number : 22
Div is 0.5454545454545454
>>> def sayHelo():
	print("Hello User")

	
>>> def sayBye(sayHelo()):
	
SyntaxError: invalid syntax
>>> def sayBye(sayHelo):
	return sayHelo

>>> sayBye()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    sayBye()
TypeError: sayBye() missing 1 required positional argument: 'sayHelo'
>>> sayBye(sayHelo)
<function sayHelo at 0x0000019BB1F2B598>
>>> h = sayBye(sayHelo)
>>> h
<function sayHelo at 0x0000019BB1F2B598>
>>> h()
Hello User
>>> def sayBye(sayHelo):
	return sayHelo()

>>> sayBye(sayHelo)
Hello User
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/calc_2.py 

1. Add
2. Sub
3. Div
4. Mul

Enter your choice : 3
Enter first number : 12
Enter second number : 22
12/22
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/calc_2.py 

1. Add
2. Sub
3. Div
4. Mul

Enter your choice : 2
Enter first number : 12
Enter second number : 22
12-22
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/calc_2.py 

1. Add
2. Sub
3. Div
4. Mul

Enter your choice : 3
Enter first number : 12
Enter second number : 22
0.5454545454545454
>>> '12' + '+' + '45'
'12+45'
>>> eval('12' + '+' + '45')
57
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/menuDriven.py 

1. Add
2. Sub
3. Div
4. Mul

Enter your choice : 7
Enter first number : 12
Enter second number : 33
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/menuDriven.py", line 29, in <module>
    operations[ch](num_1, num_2)
KeyError: '7'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/menuDriven.py 

1. Add
2. Sub
3. Div
4. Mul

Enter your choice : h
Enter first number : 12
Enter second number : 33
Invalid Choice...
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/returnStatement.py 
9
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/returnStatement.py 
(9, -1, 0.8, 20)
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/returnStatement.py 
9 -1 0.8 20
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/yield.py 
<generator object calc at 0x0000015ACE298840>
>>> calc
<function calc at 0x0000015ACE2AD268>
>>> calc(4,5)
<generator object calc at 0x0000015ACE2988B8>
>>> list(calc(4,5))
[9, -1, 0.8, 20]
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/yield.py 
<generator object calc at 0x000001320DFE8840>
>>> list(calc(4,5))
Sum is 9
Sub is -1
Div is 0.8
Mul is 20
[9, -1, 0.8, 20]
>>> x = list(calc(4,5))
Sum is 9
Sub is -1
Div is 0.8
Mul is 20
>>> x
[9, -1, 0.8, 20]
>>> for data in calc(4,5):
	print(data)

	
9
Sum is 9
-1
Sub is -1
0.8
Div is 0.8
20
Mul is 20
>>> x = []
>>> for data in calc(4,5):
	x.append(data)

	
Sum is 9
Sub is -1
Div is 0.8
Mul is 20
>>> x
[9, -1, 0.8, 20]
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/Python_WE_June_2/Functions/yield.py 
Sum is 9
Sub is -1
Div is 0.8
Mul is 20
9 -1 0.8 20
>>> x=  [5,7,7,5]
>>> a,b,c,d = x
>>> a
5
>>> b
7
>>> c
7
>>> d
5
>>> a,b,c = x
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a,b,c = x
ValueError: too many values to unpack (expected 3)
>>> a,b,*c = x
>>> a
5
>>> b
7
>>> c
[7, 5]
>>> a,*b,c = x
>>> a
5
>>> b
[7, 7]
c
>>> 
>>> c
5
>>> x
[5, 7, 7, 5]
>>> 
