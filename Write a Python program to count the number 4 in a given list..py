Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def list(number):
	count=0
	for num in number:
		if num==4:
			count=count+1
	return count

>>> print(list([1,2,3,4,5,6,4,3,12,3,5,4]))
3
>>> #Write a Python program to count the number 4 in a given list.
>>> print(list([4,4,4,4,45,5,4,5,4,5,4,5]))
7
>>> 
