Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged
>>> x=str(input("Enter a string : "))
Enter a string : lincoln
>>> if x.startswith("Is"):
	print(x)
else:
	print("Is"+x)

	
Islincoln
>>> #it can also be done another way its give n below
>>> def string(str):
	if len(str)>=2 nad str[:2]=="Is":
		
SyntaxError: invalid syntax
>>> def string(str):
	if len(str)>=2 and str[:2]=="Is":
		return str
	return "Is"+str

>>> print(string("Array"))
IsArray
>>> print(string("Isempty"))
Isempty
>>> 
