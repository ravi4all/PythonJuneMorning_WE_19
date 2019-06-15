Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> msg = "Welcome to Brain Mentors for Python Programming"
>>> len(msg)
47
>>> dir(str())
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> msg.capitalize()
'Welcome to brain mentors for python programming'
>>> msg.count('o')
6
>>> msg.count('o',0,10)
2
>>> msg.find('o')
4
>>> msg.find('o',0)
4
>>> msg.find('o',5)
9
>>> msg('o',10)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    msg('o',10)
TypeError: 'str' object is not callable
>>> msg.find('o',10)
21
>>> msg.center(10)
'Welcome to Brain Mentors for Python Programming'
>>> msg.center(20)
'Welcome to Brain Mentors for Python Programming'
>>> msg.center(40)
'Welcome to Brain Mentors for Python Programming'
>>> msg.center(50)
' Welcome to Brain Mentors for Python Programming  '
>>> msg.center(61)
'       Welcome to Brain Mentors for Python Programming       '
>>> msg.center(61,'*')
'*******Welcome to Brain Mentors for Python Programming*******'
>>> msg.upper()
'WELCOME TO BRAIN MENTORS FOR PYTHON PROGRAMMING'
>>> msg.title()
'Welcome To Brain Mentors For Python Programming'
>>> msg.rfind('o')
38
>>> msg.split()
['Welcome', 'to', 'Brain', 'Mentors', 'for', 'Python', 'Programming']
>>> m = msg.split()
>>> m
['Welcome', 'to', 'Brain', 'Mentors', 'for', 'Python', 'Programming']
>>> '-'.join(m)
'Welcome-to-Brain-Mentors-for-Python-Programming'
>>> msg.replace('o','i')
'Welcime ti Brain Mentirs fir Pythin Prigramming'
>>> msg
'Welcome to Brain Mentors for Python Programming'
>>> msg.islower()
False
>>> msg.upper()
'WELCOME TO BRAIN MENTORS FOR PYTHON PROGRAMMING'
>>> msg.isupper()
False
>>> msg.isalpha()
False
>>> msg.startswith('W')
True
>>> msg.endswith('g')
True
>>> msg
'Welcome to Brain Mentors for Python Programming'
>>> msg.zfill('*')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    msg.zfill('*')
TypeError: 'str' object cannot be interpreted as an integer
>>> msg.zfill(50,'*')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    msg.zfill(50,'*')
TypeError: zfill() takes exactly one argument (2 given)
>>> msg.zfill(50)
'000Welcome to Brain Mentors for Python Programming'
>>> msg.zfill(70)
'00000000000000000000000Welcome to Brain Mentors for Python Programming'
>>> msg.center(71,'*')
'************Welcome to Brain Mentors for Python Programming************'
>>> x = msg.center(71,'*')
>>> x
'************Welcome to Brain Mentors for Python Programming************'
>>> x.strip()
'************Welcome to Brain Mentors for Python Programming************'
>>> x.strip('*')
'Welcome to Brain Mentors for Python Programming'
>>> 
