Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> li=[1,2,3]
>>> li1=[5,6,7,8,9]
>>> li.extend(li1)
>>> li
[1, 2, 3, 5, 6, 7, 8, 9]
>>> del(li[2])
>>> li
[1, 2, 5, 6, 7, 8, 9]
>>> del(li[0])
>>> li
[2, 5, 6, 7, 8, 9]
>>> li=[]
>>> for x in range(10):
	li.append(x)

	
>>> li
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> li1=[1,2,3,4]
>>> li2=[5,6,7,8,9]
>>> li=li1+li2
>>> li
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> li3=li1*5
>>> li3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> str="".join(li)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    str="".join(li)
TypeError: sequence item 0: expected str instance, int found
>>> li=["a","b","c"]
>>> li
['a', 'b', 'c']
>>> str="".join(li)
>>> str
'abc'
>>> print(str)
abc
>>> str=" ".join(li)
>>> print(str)
a b c
>>> 
