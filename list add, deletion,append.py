Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fruits=["mango","coconut","banana"]
>>> fruits.insert(0,"apple")
>>> fruits
['apple', 'mango', 'coconut', 'banana']
>>> fruits.insert(2,"watermelon")
>>> fruits
['apple', 'mango', 'watermelon', 'coconut', 'banana']
>>> fruits.remove("watermelon")
>>> fruits
['apple', 'mango', 'coconut', 'banana']
>>> item="pineapple"
>>> if item infruits:
	
SyntaxError: invalid syntax
>>> if item in fruits:
	remove(item)

	
>>> if item in fruits:
	remove(item)
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if item in fruits:
	remove(item)
	else:
		
SyntaxError: invalid syntax
>>> if item in fruits:
	remove(item)
else:
	print(item,"not in the item")

	
pineapple not in the item
>>> item=fruit.pop(2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    item=fruit.pop(2)
NameError: name 'fruit' is not defined
>>> item=fruits.pop(2)
>>> item
'coconut'
>>> fruits
['apple', 'mango', 'banana']
>>> li=[1,2,3]
>>> li1=[3,5,2,5,6,9]
>>> li.extend(li1)
>>> li
[1, 2, 3, 3, 5, 2, 5, 6, 9]
>>> li.sort()
>>> li
[1, 2, 2, 3, 3, 5, 5, 6, 9]
>>> li2=[]
>>> for x in range(10):
	li2.append(x)

	
>>> print(li)
[1, 2, 2, 3, 3, 5, 5, 6, 9]
>>> print(li2)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
