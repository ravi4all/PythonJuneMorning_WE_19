Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = "hello there"
>>> a = 'hello there'
>>> a = "hello Ravi"
>>> print(a)
hello Ravi
>>> a = 'hello "Ravi"'
>>> print(a)
hello "Ravi"
>>> a = "hello\nRavi"
>>> print(a)
hello
Ravi
>>> a = "hello\\nRavi"
>>> print(a)
hello\nRavi
>>> a = r"hello\nRavi"
>>> print(a)
hello\nRavi
>>> a,b = 12,22
>>> a
12
>>> b
22
>>> a,b = b,a
>>> a
22
>>> b
12
>>> a = "hello everyone welcome to python programming"
>>> len(a)
44
>>> a[0]
'h'
>>> a[6]
'e'
>>> a[-1]
'g'
>>> a[0:8]
'hello ev'
>>> a[8:34]
'eryone welcome to python p'
>>> a[0:20:2]
'hloeeyn ec'
>>> a[0:20:5]
'h yw'
>>> a[10:0]
''
>>> a[10:0:-1]
'yreve olle'
>>> a[10::-1]
'yreve olleh'
>>> a[:]
'hello everyone welcome to python programming'
>>> a[10:]
'yone welcome to python programming'
>>> a[:10]
'hello ever'
>>> a[10::-1]
'yreve olleh'
>>> a[-1:-10]
''
>>> a[-1:-10:-1]
'gnimmargo'
>>> a[-10:-1]
'rogrammin'
>>> 
