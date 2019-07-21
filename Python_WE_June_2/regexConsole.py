Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> text = "hello hi hey"
>>> re.search('[\s]\w+', text)
<re.Match object; span=(5, 8), match=' hi'>
>>> re.search('\s\w+', text)
<re.Match object; span=(5, 8), match=' hi'>
>>> re.findall('\s\w+', text)
[' hi', ' hey']
>>> text = "num_1 is 9898877899, num_2 is 7899877897, num_3 is 8989897788"
>>> re.findall('[0-9]{10}', text)
['9898877899', '7899877897', '8989897788']
>>> text = ["ram122@gmail.com","123ram@gmail.com","#ram11@gmail.com","ram$21@gmail.com","ram@gmail,com"]
>>> for i in range(len(text))
SyntaxError: invalid syntax
>>> for i in range(len(text)):
	if re.search('[a-z|0-9]\w+[@]\w+[.]\w{2,3}'):
		print("Valid",text[i])
	else:
		print("Invalid",text[i])

		
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    if re.search('[a-z|0-9]\w+[@]\w+[.]\w{2,3}'):
TypeError: search() missing 1 required positional argument: 'string'
>>> for i in range(len(text)):
	if re.search('[a-z|0-9]\w+[@]\w+[.]\w{2,3}', text[i]):
		print("Valid",text[i])
	else:
		print("Invalid",text[i])

		
Valid ram122@gmail.com
Valid 123ram@gmail.com
Valid #ram11@gmail.com
Valid ram$21@gmail.com
Invalid ram@gmail,com
>>> re.search()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    re.search()
TypeError: search() missing 2 required positional arguments: 'pattern' and 'string'
>>> re.search('[a-z|0-9]\w+[@]\w+[.]\w{2,3}','$ram@gmail.com')
<re.Match object; span=(1, 14), match='ram@gmail.com'>
>>> for i in range(len(text)):
	if re.search('([^#|^$^a-z|0-9]\w+[@]\w+[.]\w{2,3})\w+', text[i]):
		print("Valid",text[i])
	else:
		print("Invalid",text[i])

		
Invalid ram122@gmail.com
Invalid 123ram@gmail.com
Invalid #ram11@gmail.com
Invalid ram$21@gmail.com
Invalid ram@gmail,com
>>> for i in range(len(text)):
	if re.search('([^#|^$|a-z|0-9]\w+[@]\w+[.]\w{2,3})\w+', text[i]):
		print("Valid",text[i])
	else:
		print("Invalid",text[i])

		
Invalid ram122@gmail.com
Invalid 123ram@gmail.com
Invalid #ram11@gmail.com
Invalid ram$21@gmail.com
Invalid ram@gmail,com
>>> for i in range(len(text)):
	if re.match('([^#|^$|a-z|0-9]\w+[@]\w+[.]\w{2,3})\w+', text[i]):
		print("Valid",text[i])
	else:
		print("Invalid",text[i])

		
Invalid ram122@gmail.com
Invalid 123ram@gmail.com
Invalid #ram11@gmail.com
Invalid ram$21@gmail.com
Invalid ram@gmail,com
>>> for i in range(len(text)):
	if re.match('([a-z|0-9]\w+[@]\w+[.]\w{2,3})\w+', text[i]):
		print("Valid",text[i])
	else:
		print("Invalid",text[i])

		
Valid ram122@gmail.com
Valid 123ram@gmail.com
Invalid #ram11@gmail.com
Invalid ram$21@gmail.com
Invalid ram@gmail,com
>>> x = {"name":"Apple","p_price":98000}
>>> for item in x:
	print(item)

	
name
p_price
>>> for item in x.values():
	print(item)

	
Apple
98000
>>> 
