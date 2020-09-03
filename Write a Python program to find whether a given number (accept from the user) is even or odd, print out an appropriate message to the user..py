Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
>>> def number(int):
	if int%2==0:
		return("the number is even")
	else:
		return("the number is odd")

	
>>> print(number(5))
the number is odd
>>> print(number(8))
the number is even
>>> 
